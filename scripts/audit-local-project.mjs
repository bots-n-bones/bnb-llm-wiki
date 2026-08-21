#!/usr/bin/env node

import { createHash } from 'node:crypto'
import { createReadStream, existsSync } from 'node:fs'
import { mkdir, readFile, readdir, stat, writeFile } from 'node:fs/promises'
import {
  basename,
  dirname,
  extname,
  join,
  relative,
  resolve,
  sep,
} from 'node:path'

const [, , inputRootArg, outputDirArg] = process.argv
if (!inputRootArg || !outputDirArg) {
  console.error(
    'Usage: node scripts/audit-local-project.mjs <input-root> <output-dir>',
  )
  process.exit(2)
}

const inputRoot = resolve(inputRootArg)
const outputDir = resolve(outputDirArg)
if (!existsSync(inputRoot))
  throw new Error(`Input root does not exist: ${inputRoot}`)

const capturedAt = new Date().toISOString()
const snapshotId = `bnb-local-${capturedAt.replace(/[-:.]/g, '').replace('Z', 'Z')}`
const manifestPath = join(outputDir, 'bnb-local-manifest.jsonl')
const duplicatesPath = join(outputDir, 'bnb-local-duplicate-groups.jsonl')
const conflictsPath = join(outputDir, 'bnb-local-path-conflicts.jsonl')
const summaryJsonPath = join(outputDir, 'bnb-local-scan-summary.json')
const summaryMdPath = join(outputDir, 'bnb-local-audit.md')

const mimeByExtension = new Map([
  ['.md', 'text/markdown'],
  ['.txt', 'text/plain'],
  ['.csv', 'text/csv'],
  ['.json', 'application/json'],
  ['.yaml', 'application/yaml'],
  ['.yml', 'application/yaml'],
  ['.html', 'text/html'],
  ['.htm', 'text/html'],
  ['.pdf', 'application/pdf'],
  ['.doc', 'application/msword'],
  [
    '.docx',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  ],
  ['.xls', 'application/vnd.ms-excel'],
  [
    '.xlsx',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  ],
  ['.xlsm', 'application/vnd.ms-excel.sheet.macroEnabled.12'],
  ['.xlsb', 'application/vnd.ms-excel.sheet.binary.macroEnabled.12'],
  ['.ppt', 'application/vnd.ms-powerpoint'],
  [
    '.pptx',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  ],
  ['.png', 'image/png'],
  ['.jpg', 'image/jpeg'],
  ['.jpeg', 'image/jpeg'],
  ['.webp', 'image/webp'],
  ['.svg', 'image/svg+xml'],
  ['.mp3', 'audio/mpeg'],
  ['.m4a', 'audio/mp4'],
  ['.wav', 'audio/wav'],
  ['.mp4', 'video/mp4'],
  ['.mov', 'video/quicktime'],
  ['.zip', 'application/zip'],
  ['.7z', 'application/x-7z-compressed'],
  ['.gz', 'application/gzip'],
  ['.tar', 'application/x-tar'],
])

const technicalParts = new Set([
  'node_modules',
  '.git',
  'dist',
  'build',
  '.cache',
  '__pycache__',
  '.next',
  '.vite',
])
const archiveExtensions = new Set(['.zip', '.7z', '.gz', '.tar', '.rar'])
const macroExtensions = new Set(['.xlsm', '.xlsb', '.docm', '.pptm'])
const textMimeTypes = new Set([
  'text/markdown',
  'text/plain',
  'text/csv',
  'text/html',
  'application/json',
  'application/yaml',
])
const textExtensions = new Set([
  '.css',
  '.js',
  '.mjs',
  '.cjs',
  '.ts',
  '.tsx',
  '.py',
  '.rb',
  '.sh',
])
const credentialPatterns = [
  /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/,
  /gh[pousr]_[A-Za-z0-9]{30,}/,
  /sk-(?:proj-)?[A-Za-z0-9_-]{20,}/,
  /AKIA[0-9A-Z]{16}/,
  /AIza[0-9A-Za-z_-]{30,}/,
  /(?:bot)?\d{5,}:[A-Za-z0-9_-]{20,}/i,
  /Bearer\s+[A-Za-z0-9._~+/-]{20,}/i,
]
const secretNamePattern =
  /^(?:\.env(?:\..+)?|credentials?(?:\..+)?|secrets?(?:\..+)?|tokens?(?:\..+)?|api[-_ ]?keys?(?:\..+)?)$/i
const archivePathPattern =
  /(?:^|\/)(?:99[^/]*archive|archive|backups?|06_old_notion)(?:\/|$)/i
const copyNamePattern = /(?:\s\(\d+\)|[-_ ]copy|[-_ ]копия)(?=\.[^.]+$|$)/i

function toPosix(value) {
  return value.split(sep).join('/')
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

function initialClassification(path, rel) {
  const parts = rel.split('/')
  const name = basename(path)
  const extension = extname(name).toLowerCase()
  if (
    parts.some((part) => technicalParts.has(part)) ||
    name === '.DS_Store' ||
    name.startsWith('~$')
  ) {
    return { classification: 'out-of-scope', reason: 'technical-or-temporary' }
  }
  if (name === 'Content-os-project v0002.zip') {
    return {
      classification: 'out-of-scope',
      reason: 'explicitly-excluded-archive',
    }
  }
  if (macroExtensions.has(extension)) {
    return {
      classification: 'restricted',
      reason: 'macro-capable-office-format',
    }
  }
  if (/^\.env(?:\..+)?$/i.test(name) && /example|sample|template/i.test(name)) {
    return {
      classification: 'out-of-scope',
      reason: 'environment-example-not-indexed',
    }
  }
  if (secretNamePattern.test(name)) {
    return {
      classification: 'restricted',
      reason: 'secret-bearing-name-candidate',
    }
  }
  if (archiveExtensions.has(extension) || archivePathPattern.test(rel)) {
    return {
      classification: 'archive-only',
      reason: archiveExtensions.has(extension)
        ? 'archive-not-extracted'
        : 'archive-path',
    }
  }
  return {
    classification: 'supporting-source',
    reason: 'registered-local-source',
  }
}

async function collectFiles(directory, output = []) {
  const entries = await readdir(directory, { withFileTypes: true })
  entries.sort((left, right) => left.name.localeCompare(right.name, 'en'))
  for (const entry of entries) {
    const path = join(directory, entry.name)
    if (entry.isSymbolicLink()) {
      output.push({ path, symlink: true })
    } else if (entry.isDirectory()) {
      await collectFiles(path, output)
    } else if (entry.isFile()) {
      output.push({ path, symlink: false })
    }
  }
  return output
}

const files = await collectFiles(inputRoot)
const records = []
for (const [index, item] of files.entries()) {
  const rel = toPosix(relative(inputRoot, item.path))
  const info = await stat(item.path)
  const initial = initialClassification(item.path, rel)
  const checksum = item.symlink ? null : await sha256(item.path)
  const mimeType =
    mimeByExtension.get(extname(item.path).toLowerCase()) ??
    'application/octet-stream'
  const contentFlags = []
  if (
    !item.symlink &&
    initial.classification === 'supporting-source' &&
    (textMimeTypes.has(mimeType) ||
      textExtensions.has(extname(item.path).toLowerCase())) &&
    info.size <= 10_000_000
  ) {
    const text = await readFile(item.path, 'utf8')
    if (credentialPatterns.some((pattern) => pattern.test(text))) {
      initial.classification = 'restricted'
      initial.reason = 'credential-pattern-in-text'
      contentFlags.push('credential-pattern')
    }
  }
  records.push({
    snapshot_id: snapshotId,
    captured_at: capturedAt,
    local_file_id: checksum
      ? `local:sha256:${checksum}`
      : `local:symlink:${createHash('sha256').update(rel).digest('hex')}`,
    name: basename(item.path),
    original_path: rel,
    absolute_path: item.path,
    parent_path: toPosix(dirname(rel)),
    mime_type: mimeType,
    size: info.size,
    modified_time: info.mtime.toISOString(),
    checksum: checksum ? `sha256:${checksum}` : null,
    revision_id: checksum ? `sha256:${checksum}` : null,
    classification: initial.classification,
    classification_reason: initial.reason,
    duplicate_group: null,
    preferred_candidate: false,
    content_flags: contentFlags,
    symlink: item.symlink,
  })
  if ((index + 1) % 1000 === 0)
    console.error(`Hashed ${index + 1}/${files.length}`)
}

const byChecksum = new Map()
for (const record of records) {
  if (!record.checksum) continue
  const group = byChecksum.get(record.checksum) ?? []
  group.push(record)
  byChecksum.set(record.checksum, group)
}

const duplicateGroups = []
let duplicateIndex = 0
for (const members of byChecksum.values()) {
  if (members.length < 2) continue
  duplicateIndex += 1
  const groupId = `bnb-local-exact-${String(duplicateIndex).padStart(5, '0')}`
  const preferred = [...members].sort((left, right) => {
    const rank = (record) => {
      let score = 0
      if (record.original_path.startsWith('bots-n-bones/')) score += 100
      if (record.classification === 'supporting-source') score += 30
      if (!copyNamePattern.test(record.name)) score += 10
      score -= record.original_path.length / 10000
      return score
    }
    return (
      rank(right) - rank(left) ||
      right.modified_time.localeCompare(left.modified_time)
    )
  })[0]
  for (const member of members) {
    member.duplicate_group = groupId
    member.preferred_candidate = member === preferred
    if (member !== preferred && member.classification === 'supporting-source') {
      member.classification = 'duplicate-candidate'
      member.classification_reason = 'exact-checksum-duplicate'
    }
  }
  duplicateGroups.push({
    duplicate_group: groupId,
    checksum: preferred.checksum,
    size: preferred.size,
    preferred_candidate_path: preferred.original_path,
    member_count: members.length,
    members: members.map((member) => member.original_path),
  })
}

records.sort((left, right) =>
  left.original_path.localeCompare(right.original_path, 'en'),
)
duplicateGroups.sort(
  (left, right) =>
    right.member_count - left.member_count ||
    left.duplicate_group.localeCompare(right.duplicate_group),
)

function logicalPath(record) {
  const parts = record.original_path.split('/')
  if (/^bots-n-bones(?: [234])?$/.test(parts[0])) parts.shift()
  return parts.join('/').normalize('NFC').toLocaleLowerCase('en-US')
}

const byLogicalPath = new Map()
for (const record of records) {
  const key = logicalPath(record)
  const group = byLogicalPath.get(key) ?? []
  group.push(record)
  byLogicalPath.set(key, group)
}
const pathConflicts = []
let conflictIndex = 0
for (const [pathKey, members] of byLogicalPath.entries()) {
  if (members.every((member) => member.classification === 'out-of-scope'))
    continue
  const checksums = new Set(
    members.map((member) => member.checksum).filter(Boolean),
  )
  if (checksums.size < 2) continue
  conflictIndex += 1
  pathConflicts.push({
    conflict_group: `bnb-local-conflict-${String(conflictIndex).padStart(5, '0')}`,
    logical_path: pathKey,
    member_count: members.length,
    checksum_count: checksums.size,
    members: members.map((member) => ({
      original_path: member.original_path,
      checksum: member.checksum,
      size: member.size,
      modified_time: member.modified_time,
      classification: member.classification,
    })),
  })
}

const countBy = (field) =>
  Object.fromEntries(
    [
      ...records
        .reduce(
          (map, record) =>
            map.set(record[field], (map.get(record[field]) ?? 0) + 1),
          new Map(),
        )
        .entries(),
    ].sort(),
  )
const duplicateMembers = records.filter(
  (record) => record.duplicate_group,
).length
const duplicateRedundantBytes = duplicateGroups.reduce(
  (sum, group) => sum + group.size * (group.member_count - 1),
  0,
)
const totalBytes = records.reduce((sum, record) => sum + record.size, 0)
const summary = {
  snapshot_id: snapshotId,
  captured_at: capturedAt,
  input_root: inputRoot,
  file_count: records.length,
  total_bytes: totalBytes,
  exact_duplicate_groups: duplicateGroups.length,
  exact_duplicate_members: duplicateMembers,
  exact_duplicate_redundant_bytes: duplicateRedundantBytes,
  same_path_content_conflicts: pathConflicts.length,
  classification_counts: countBy('classification'),
  mime_type_counts: countBy('mime_type'),
  mutations_performed: false,
  archives_extracted: false,
}

const md = `---\nschema: hermes-kb/v2\nid: audit-bnb-local-${capturedAt.slice(0, 10)}\ntitle: BnB local project audit\ntype: reference\nstatus: active\ncanonical: false\nowner: ilya\nconfidentiality: internal\ncreated: ${capturedAt.slice(0, 10)}\nupdated: ${capturedAt.slice(0, 10)}\ntags: [audit, local-source, deduplication]\n---\n\n# BnB local project audit\n\nRead-only inventory of the downloaded BnB project. No source file was moved, renamed, deleted, opened as an application, or extracted from an archive. Checksums are content hashes, not business approval.\n\n- Files: **${records.length.toLocaleString('en-US')}**\n- Bytes: **${totalBytes.toLocaleString('en-US')}**\n- Exact duplicate groups: **${duplicateGroups.length.toLocaleString('en-US')}**\n- Files participating in exact duplicate groups: **${duplicateMembers.toLocaleString('en-US')}**\n- Redundant bytes represented by exact duplicates: **${duplicateRedundantBytes.toLocaleString('en-US')}**\n- Same logical path with different content: **${pathConflicts.length.toLocaleString('en-US')}**\n\n## Classification\n\n${Object.entries(
  summary.classification_counts,
)
  .map(([key, value]) => `- ${key}: ${value.toLocaleString('en-US')}`)
  .join(
    '\n',
  )}\n\n## Safety and interpretation\n\n- Duplicate status is based only on identical SHA-256 content.\n- A preferred candidate is a deterministic review suggestion, not an approved deletion target.\n- Archives were not extracted.\n- Files with secret-like names are restricted candidates and must not enter the search index.\n- Business-level near-duplicates and superseded versions still require semantic review.\n`

await mkdir(outputDir, { recursive: true })
await writeFile(
  manifestPath,
  `${records.map((record) => JSON.stringify(record)).join('\n')}\n`,
)
await writeFile(
  duplicatesPath,
  `${duplicateGroups.map((group) => JSON.stringify(group)).join('\n')}\n`,
)
await writeFile(
  conflictsPath,
  `${(pathConflicts.length
    ? pathConflicts
    : [
        {
          record_type: 'summary',
          snapshot_id: snapshotId,
          conflict_count: 0,
          notes:
            'No non-technical same-logical-path content conflicts detected.',
        },
      ]
  )
    .map((group) => JSON.stringify(group))
    .join('\n')}\n`,
)
await writeFile(summaryJsonPath, `${JSON.stringify(summary, null, 2)}\n`)
await writeFile(summaryMdPath, md)
console.log(JSON.stringify(summary, null, 2))
