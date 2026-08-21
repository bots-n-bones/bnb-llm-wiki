#!/usr/bin/env node

import { createHash } from 'node:crypto'
import { constants, createReadStream, existsSync } from 'node:fs'
import {
  copyFile,
  mkdir,
  readFile,
  stat,
  utimes,
  writeFile,
} from 'node:fs/promises'
import { dirname, join, relative, resolve, sep } from 'node:path'

const args = process.argv.slice(2)
const apply = args.includes('--apply')
const positional = args.filter((arg) => arg !== '--apply')
const [manifestArg, destinationArg, receiptArg] = positional
if (!manifestArg || !destinationArg || !receiptArg) {
  console.error(
    'Usage: node scripts/materialize-local-canonical.mjs <manifest.jsonl> <destination> <receipt.jsonl> [--apply]',
  )
  process.exit(2)
}

const manifestPath = resolve(manifestArg)
const destinationRoot = resolve(destinationArg)
const receiptPath = resolve(receiptArg)
if (
  destinationRoot === '/' ||
  destinationRoot === resolve(process.env.HOME || '/invalid')
) {
  throw new Error('Unsafe canonical destination')
}

const records = (await readFile(manifestPath, 'utf8'))
  .split(/\r?\n/)
  .filter(Boolean)
  .map((line) => JSON.parse(line))
  .filter(
    (record) =>
      record.classification === 'supporting-source' && !record.symlink,
  )

function destinationRelativePath(originalPath) {
  const parts = originalPath.split('/')
  if (/^bots-n-bones(?: [234])?$/.test(parts[0])) parts.shift()
  const value = parts.join('/')
  if (!value || value.startsWith('/') || value.split('/').includes('..')) {
    throw new Error(`Unsafe manifest path: ${originalPath}`)
  }
  return value
}

function sha256(path) {
  return new Promise((resolveHash, reject) => {
    const hash = createHash('sha256')
    const stream = createReadStream(path)
    stream.on('error', reject)
    stream.on('data', (chunk) => hash.update(chunk))
    stream.on('end', () => resolveHash(hash.digest('hex')))
  })
}

const planned = []
const destinations = new Map()
for (const record of records) {
  const relativePath = destinationRelativePath(record.original_path)
  const destination = resolve(destinationRoot, relativePath)
  if (relative(destinationRoot, destination).startsWith(`..${sep}`)) {
    throw new Error(
      `Destination escapes canonical root: ${record.original_path}`,
    )
  }
  const existing = destinations.get(destination)
  if (existing && existing.checksum !== record.checksum) {
    throw new Error(`Conflicting source content for ${relativePath}`)
  }
  if (!existing) destinations.set(destination, record)
}

for (const [destination, record] of destinations.entries()) {
  const expected = String(record.checksum || '').replace(/^sha256:/, '')
  if (!expected) throw new Error(`Missing checksum for ${record.original_path}`)
  let action = 'copy'
  if (existsSync(destination)) {
    const actual = await sha256(destination)
    if (actual !== expected)
      throw new Error(`Existing destination conflicts: ${destination}`)
    action = 'already-present'
  }
  planned.push({
    action,
    source_path: record.absolute_path,
    source_original_path: record.original_path,
    destination_path: destination,
    destination_relative_path: relative(destinationRoot, destination)
      .split(sep)
      .join('/'),
    checksum: record.checksum,
    size: record.size,
    modified_time: record.modified_time,
  })
}

if (apply) {
  await mkdir(destinationRoot, { recursive: true })
  for (const [index, item] of planned.entries()) {
    if (item.action === 'copy') {
      await mkdir(dirname(item.destination_path), { recursive: true })
      await copyFile(
        item.source_path,
        item.destination_path,
        constants.COPYFILE_FICLONE,
      )
      const copiedHash = await sha256(item.destination_path)
      if (`sha256:${copiedHash}` !== item.checksum) {
        throw new Error(
          `Post-copy checksum mismatch: ${item.destination_relative_path}`,
        )
      }
      const sourceInfo = await stat(item.source_path)
      await utimes(item.destination_path, sourceInfo.atime, sourceInfo.mtime)
    }
    if ((index + 1) % 500 === 0)
      console.error(`Materialized ${index + 1}/${planned.length}`)
  }
}

const receipt = {
  generated_at: new Date().toISOString(),
  mode: apply ? 'apply' : 'dry-run',
  manifest_path: manifestPath,
  destination_root: destinationRoot,
  source_count: records.length,
  destination_count: planned.length,
  bytes: planned.reduce((sum, item) => sum + Number(item.size || 0), 0),
  copied: planned.filter((item) => item.action === 'copy').length,
  already_present: planned.filter((item) => item.action === 'already-present')
    .length,
}
await mkdir(dirname(receiptPath), { recursive: true })
await writeFile(
  receiptPath,
  `${planned.map((item) => JSON.stringify(item)).join('\n')}\n`,
)
await writeFile(
  receiptPath.replace(/\.jsonl$/i, '-summary.json'),
  `${JSON.stringify(receipt, null, 2)}\n`,
)
console.log(JSON.stringify(receipt, null, 2))
