import fs from 'node:fs'
import path from 'node:path'
import process from 'node:process'
import Ajv2020 from 'ajv/dist/2020.js'
import addFormats from 'ajv-formats'
import YAML from 'yaml'

const root = path.resolve(process.cwd())
const ignoredDirectories = new Set(['.git', 'node_modules', '.local-index'])
const forbiddenDirectories = new Set(['dist', 'build'])
const forbiddenExtensions = new Set([
  '.7z', '.avi', '.doc', '.docx', '.gif', '.gz', '.jpeg', '.jpg', '.mov',
  '.mp3', '.mp4', '.pdf', '.png', '.ppt', '.pptx', '.sqlite', '.sqlite3',
  '.tar', '.webp', '.xls', '.xlsx', '.zip',
])
const requiredFields = [
  'schema', 'id', 'title', 'type', 'status', 'canonical', 'owner',
  'confidentiality', 'created', 'updated', 'tags',
]
const portfolioProjects = [
  'svmpx', 'hello-i-am', 'content-os', 'bots-n-bones', 'quntm', 'ursus',
  'shared',
]
const requiredProjectLayers = [
  '00-canon', '01-knowledge', '02-decisions', '03-sops',
  '04-source-register', '90-derived', '99-archive',
]
const sourceProvenanceFields = [
  'drive_file_id', 'url', 'mime_type', 'parent_folder_id', 'original_path',
  'original_title', 'modified_time',
]
const sourceFingerprintFields = ['checksum', 'revision_id']
const excludedManifestClassifications = new Set([
  'restricted', 'archive-only', 'superseded-candidate',
])
const secretPatterns = [
  /-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----/,
  /\b(?:gh[opsu]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b/,
  /\bsk-[A-Za-z0-9_-]{20,}\b/,
  /\b(?:sk|rk)_live_[A-Za-z0-9]{20,}\b/,
  /\bAIza[0-9A-Za-z_-]{30,}\b/,
  /\bAKIA[0-9A-Z]{16}\b/,
  /\b(?:xox[baprs]-|glpat-|npm_|lin_api_)[A-Za-z0-9_-]{20,}\b/,
  /\bBearer\s+[A-Za-z0-9._~-]{24,}\b/i,
  /\b(?:bot)?\d{5,12}:[A-Za-z0-9_-]{30,}\b/i,
]

const errors = []
const warnings = []
const markdownFiles = []
const jsonlFiles = []
const textFiles = []

function relative(filePath) {
  return path.relative(root, filePath).replace(/\\/g, '/')
}

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'))
  } catch (error) {
    errors.push(`${relative(filePath)}: invalid JSON: ${error.message}`)
    return null
  }
}

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (ignoredDirectories.has(entry.name)) continue
    const fullPath = path.join(directory, entry.name)
    if (entry.isDirectory()) {
      if (forbiddenDirectories.has(entry.name)) {
        errors.push(`${relative(fullPath)}: forbidden generated directory`)
        continue
      }
      walk(fullPath)
      continue
    }

    const extension = path.extname(entry.name).toLowerCase()
    if (forbiddenExtensions.has(extension)) {
      errors.push(`${relative(fullPath)}: binary originals are forbidden`)
    }
    if (entry.name === '.env' || entry.name.startsWith('.env.')) {
      errors.push(`${relative(fullPath)}: environment files are forbidden`)
    }
    if (extension === '.md') markdownFiles.push(fullPath)
    if (extension === '.jsonl') jsonlFiles.push(fullPath)
    if (
      !forbiddenExtensions.has(extension) &&
      (extension === '' || [
        '.cjs', '.css', '.csv', '.html', '.js', '.json', '.jsonl', '.md',
        '.mjs', '.sh', '.toml', '.ts', '.tsx', '.txt', '.xml', '.yml', '.yaml',
      ].includes(extension))
    ) {
      textFiles.push(fullPath)
    }
    if (extension === '.json') readJson(fullPath)
  }
}

walk(root)

const projectsDirectory = path.join(root, 'projects')
if (!fs.existsSync(projectsDirectory) || !fs.statSync(projectsDirectory).isDirectory()) {
  errors.push('projects: missing governed project directory')
} else {
  for (const entry of fs.readdirSync(projectsDirectory, { withFileTypes: true })) {
    if (entry.isDirectory() && !portfolioProjects.includes(entry.name)) {
      errors.push(`projects/${entry.name}: project scaffold is not governed`)
    }
  }
}

for (const project of portfolioProjects) {
  const projectRoot = path.join(root, 'projects', project)
  if (!fs.existsSync(projectRoot)) {
    errors.push(`projects/${project}: missing project scaffold`)
    continue
  }
  if (!fs.statSync(projectRoot).isDirectory()) {
    errors.push(`projects/${project}: project scaffold must be a directory`)
    continue
  }
  if (!fs.existsSync(path.join(projectRoot, 'README.md'))) {
    errors.push(`projects/${project}: missing project home README.md`)
  }
  for (const layer of requiredProjectLayers) {
    const layerPath = path.join(projectRoot, layer)
    if (!fs.existsSync(layerPath)) {
      errors.push(`projects/${project}/${layer}: missing required project layer`)
    } else if (!fs.statSync(layerPath).isDirectory()) {
      errors.push(`projects/${project}/${layer}: required project layer must be a directory`)
    }
  }
}

const ajv = new Ajv2020({ allErrors: true, strict: false })
addFormats(ajv)
const frontmatterSchema = readJson(path.join(root, 'schemas/frontmatter.schema.json'))
const driveManifestSchema = readJson(path.join(root, 'schemas/drive-manifest-record.schema.json'))
const validateFrontmatter = frontmatterSchema ? ajv.compile(frontmatterSchema) : null
const validateDriveManifest = driveManifestSchema ? ajv.compile(driveManifestSchema) : null
const manifestClassificationsByDriveId = new Map()

for (const filePath of jsonlFiles) {
  const file = relative(filePath)
  const isDriveManifest = /drive-manifest-.*\.jsonl$/i.test(file)
  let records = 0
  for (const [index, line] of fs.readFileSync(filePath, 'utf8').split(/\r?\n/).entries()) {
    if (!line.trim()) continue
    let record
    try {
      record = JSON.parse(line)
    } catch (error) {
      errors.push(`${file}:${index + 1}: invalid JSONL: ${error.message}`)
      continue
    }
    records += 1
    if (isDriveManifest && validateDriveManifest && !validateDriveManifest(record)) {
      for (const issue of validateDriveManifest.errors ?? []) {
        errors.push(`${file}:${index + 1}: manifest schema ${issue.instancePath || '/'} ${issue.message}`)
      }
    }
    if (isDriveManifest && typeof record.drive_file_id === 'string' && typeof record.classification === 'string') {
      const classifications = manifestClassificationsByDriveId.get(record.drive_file_id) ?? new Set()
      classifications.add(record.classification)
      manifestClassificationsByDriveId.set(record.drive_file_id, classifications)
    }
  }
  if (records === 0) errors.push(`${file}: JSONL file is empty`)
}

const ids = new Map()
const paths = new Set(
  markdownFiles.map((filePath) => relative(filePath).replace(/\.md$/i, '')),
)
const basenameOwners = new Map()
const metadataByFile = new Map()

for (const filePath of markdownFiles) {
  const file = relative(filePath)
  const basename = path.basename(file, '.md').toLowerCase()
  const owners = basenameOwners.get(basename) ?? []
  owners.push(file)
  basenameOwners.set(basename, owners)

  const raw = fs.readFileSync(filePath, 'utf8')
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/)
  if (!match) {
    errors.push(`${file}: missing YAML frontmatter`)
    continue
  }

  let metadata
  try {
    metadata = YAML.parse(match[1])
  } catch (error) {
    errors.push(`${file}: invalid YAML: ${error.message}`)
    continue
  }

  if (!metadata || typeof metadata !== 'object') {
    errors.push(`${file}: frontmatter must be an object`)
    continue
  }
  metadataByFile.set(file, metadata)

  for (const field of requiredFields) {
    if (!(field in metadata) || metadata[field] === null || metadata[field] === '') {
      errors.push(`${file}: missing required field ${field}`)
    }
  }

  if (validateFrontmatter && !validateFrontmatter(metadata)) {
    for (const issue of validateFrontmatter.errors ?? []) {
      errors.push(`${file}: frontmatter schema ${issue.instancePath || '/'} ${issue.message}`)
    }
  }
  if (typeof metadata.id === 'string') {
    if (ids.has(metadata.id)) {
      errors.push(`${file}: duplicate id ${metadata.id}; first used by ${ids.get(metadata.id)}`)
    } else {
      ids.set(metadata.id, file)
    }
  }
  if (!Array.isArray(metadata.tags)) errors.push(`${file}: tags must be an array`)
  if (metadata.canonical === true && metadata.status !== 'active') {
    errors.push(`${file}: canonical pages must have status active`)
  }
  if (metadata.type === 'derived' || metadata.type === 'project-home') {
    if (metadata.status !== 'draft') {
      errors.push(`${file}: ${metadata.type} pages must have status draft`)
    }
    if (metadata.canonical !== false) {
      errors.push(`${file}: ${metadata.type} pages cannot be canonical`)
    }
  }
  if (metadata.type === 'source-record') {
    for (const field of sourceProvenanceFields) {
      if (!metadata.source?.[field]) errors.push(`${file}: source.${field} is required`)
    }
    for (const field of sourceFingerprintFields) {
      if (!(field in (metadata.source ?? {}))) {
        errors.push(`${file}: source.${field} must be recorded, using null when unavailable`)
      }
    }
  }
  if (metadata.type === 'canon' && (!Array.isArray(metadata.source_ids) || metadata.source_ids.length === 0)) {
    errors.push(`${file}: canon pages must declare at least one source_id`)
  }
  if (metadata.type === 'derived') {
    if (!Array.isArray(metadata.source_ids) || metadata.source_ids.length === 0) {
      errors.push(`${file}: derived pages must declare at least one source_id`)
    }
    for (const field of ['method', 'generated_at']) {
      if (!metadata.derived?.[field]) errors.push(`${file}: derived.${field} is required`)
    }
  }
  if (metadata.related !== undefined) {
    if (!Array.isArray(metadata.related)) {
      errors.push(`${file}: related must be an array`)
    } else {
      for (const related of metadata.related) {
        if (typeof related !== 'string' || !related.trim()) {
          errors.push(`${file}: related entries must be non-empty strings`)
          continue
        }
        const target = related
          .trim()
          .replace(/^\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]$/, '$1')
          .replace(/\.md$/i, '')
        if (!target.includes('/')) {
          errors.push(`${file}: related entries must be path-qualified: ${related}`)
        } else if (!paths.has(target)) {
          errors.push(`${file}: related target does not resolve: ${target}`)
        }
      }
    }
  }

  for (const link of raw.matchAll(/\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]/g)) {
    const target = link[1].trim().replace(/\.md$/i, '')
    if (!target.includes('/')) {
      errors.push(`${file}: wiki link must be path-qualified: ${target}`)
    }
    if (!paths.has(target)) errors.push(`${file}: broken wiki link: ${target}`)
  }
}

for (const [file, metadata] of metadataByFile) {
  if (metadata.source_ids === undefined) continue
  if (!Array.isArray(metadata.source_ids)) {
    errors.push(`${file}: source_ids must be an array`)
    continue
  }
  for (const sourceId of metadata.source_ids) {
    if (typeof sourceId !== 'string' || !sourceId.trim()) {
      errors.push(`${file}: source_ids entries must be non-empty strings`)
      continue
    }
    const targetFile = ids.get(sourceId)
    if (!targetFile) {
      errors.push(`${file}: source_id does not resolve: ${sourceId}`)
      continue
    }
    if (metadataByFile.get(targetFile)?.type !== 'source-record') {
      errors.push(`${file}: source_id target is not a source-record: ${sourceId}`)
      continue
    }
    const source = metadataByFile.get(targetFile)?.source ?? {}
    for (const field of sourceProvenanceFields.slice(3)) {
      if (!source[field]) {
        errors.push(`${targetFile}: source.${field} is required because ${file} references it`)
      }
    }
    for (const field of sourceFingerprintFields) {
      if (!(field in source)) {
        errors.push(`${targetFile}: source.${field} must be recorded because ${file} references it`)
      }
    }
    for (const classification of manifestClassificationsByDriveId.get(source.drive_file_id) ?? []) {
      if (excludedManifestClassifications.has(classification)) {
        errors.push(`${file}: source_id ${sourceId} has excluded Drive manifest classification ${classification}`)
      }
    }
  }
}

for (const filePath of textFiles) {
  const content = fs.readFileSync(filePath, 'utf8')
  for (const pattern of secretPatterns) {
    if (pattern.test(content)) {
      errors.push(`${relative(filePath)}: possible credential matched ${pattern.source}`)
    }
  }
}

for (const [basename, owners] of basenameOwners) {
  if (owners.length > 1) {
    warnings.push(`ambiguous basename ${basename}: ${owners.join(', ')}`)
  }
}

console.log(
  `Validated ${markdownFiles.length} Markdown files, ${ids.size} unique IDs, and ${jsonlFiles.length} JSONL files.`,
)
for (const warning of warnings) console.warn(`WARN: ${warning}`)
for (const error of errors) console.error(`ERROR: ${error}`)
if (errors.length > 0) process.exit(1)
