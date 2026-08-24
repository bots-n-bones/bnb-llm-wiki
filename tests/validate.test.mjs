import assert from 'node:assert/strict'
import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import test from 'node:test'
import { fileURLToPath } from 'node:url'

const knowledgeRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const validator = path.join(knowledgeRoot, 'scripts', 'validate.mjs')
const portfolioProjects = [
  'svmpx', 'hello-i-am', 'content-os', 'bots-n-bones', 'quntm', 'ursus',
  'hermes', 'shared',
]
const requiredProjectLayers = [
  '00-canon', '01-knowledge', '02-decisions', '03-sops',
  '04-source-register', '90-derived', '99-archive',
]

function frontmatter(fields, body = '# Fixture') {
  return `---\n${fields}\n---\n\n${body}\n`
}

function baseFields({ id, type, extra = '' }) {
  return `schema: hermes-kb/v2
id: ${id}
title: Fixture ${id}
project: shared
type: ${type}
status: draft
canonical: false
owner: validator-test
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [fixture]${extra}`
}

function createFixture(files) {
  const fixtureRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'kb-validator-'))
  fs.mkdirSync(path.join(fixtureRoot, 'schemas'), { recursive: true })
  for (const schema of ['frontmatter.schema.json', 'drive-manifest-record.schema.json']) {
    fs.copyFileSync(path.join(knowledgeRoot, 'schemas', schema), path.join(fixtureRoot, 'schemas', schema))
  }
  for (const project of portfolioProjects) {
    const projectRoot = path.join(fixtureRoot, 'projects', project)
    fs.mkdirSync(projectRoot, { recursive: true })
    fs.writeFileSync(path.join(projectRoot, 'README.md'), frontmatter(baseFields({
      id: `fixture-${project}`,
      type: 'project-home',
    }).replace('project: shared', `project: ${project}`)))
    for (const layer of requiredProjectLayers) {
      fs.mkdirSync(path.join(projectRoot, layer), { recursive: true })
    }
  }
  for (const [relativePath, content] of Object.entries(files)) {
    const filePath = path.join(fixtureRoot, relativePath)
    fs.mkdirSync(path.dirname(filePath), { recursive: true })
    fs.writeFileSync(filePath, content)
  }
  return fixtureRoot
}

function validate(files, mutate) {
  const fixtureRoot = createFixture(files)
  try {
    mutate?.(fixtureRoot)
    execFileSync(process.execPath, [validator], {
      cwd: fixtureRoot,
      encoding: 'utf8',
      stdio: 'pipe',
    })
    return { status: 0, output: '' }
  } catch (error) {
    return {
      status: error.status ?? 1,
      output: `${error.stdout ?? ''}${error.stderr ?? ''}`,
    }
  } finally {
    fs.rmSync(fixtureRoot, { recursive: true, force: true })
  }
}

const completeSource = frontmatter(baseFields({
  id: 'src-fixture',
  type: 'source-record',
  extra: `
source:
  kind: google-drive
  drive_file_id: fixture-drive-id
  url: https://drive.google.com/file/d/fixture-drive-id/view
  mime_type: text/markdown
  parent_folder_id: fixture-parent
  original_path: fixture/source.md
  original_title: source.md
  modified_time: 2026-08-20T00:00:00Z
  checksum: null
  revision_id: null`,
}))

const activeSource = completeSource.replace('status: draft', 'status: active')

function completeDerived({ status = 'draft', canonical = false } = {}) {
  return frontmatter(baseFields({
    id: 'derived-fixture',
    type: 'derived',
    extra: `
source_ids:
  - src-fixture
derived:
  method: fixture-extractor
  generated_at: 2026-08-20T00:00:00Z`,
  }).replace('status: draft', `status: ${status}`).replace('canonical: false', `canonical: ${canonical}`))
}

function manifestRecord(classification) {
  return JSON.stringify({
    snapshot_id: 'fixture-snapshot',
    captured_at: '2026-08-20T00:00:00Z',
    drive_file_id: 'fixture-drive-id',
    name: 'fixture-source',
    original_path: 'fixture/source.md',
    mime_type: 'text/markdown',
    url: 'https://drive.google.com/file/d/fixture-drive-id/view',
    classification,
    duplicate_group: null,
    preferred_source_id: null,
    notes: null,
  })
}

test('accepts a complete governed fixture with an active source record', () => {
  const result = validate({
    'records/source.md': activeSource,
    'records/derived.md': completeDerived(),
  })

  assert.equal(result.status, 0, result.output)
})

test('rejects extra project directories outside the governed portfolio', () => {
  const result = validate({}, (fixtureRoot) => {
    fs.mkdirSync(path.join(fixtureRoot, 'projects', 'unapproved-project'))
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /projects\/unapproved-project: project scaffold is not governed/)
})

test('rejects project layers implemented as files instead of directories', () => {
  const result = validate({}, (fixtureRoot) => {
    const layer = path.join(fixtureRoot, 'projects', 'shared', '00-canon')
    fs.rmSync(layer, { recursive: true, force: true })
    fs.writeFileSync(layer, 'not a directory')
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /projects\/shared\/00-canon: required project layer must be a directory/)
})

test('rejects source records without complete provenance outside the legacy supporting path', () => {
  const result = validate({
    'records/source.md': frontmatter(baseFields({
      id: 'src-fixture',
      type: 'source-record',
      extra: `
source:
  kind: google-drive
  drive_file_id: fixture-drive-id
  url: https://drive.google.com/file/d/fixture-drive-id/view
  mime_type: text/markdown`,
    })),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /source\.parent_folder_id is required/)
})

test('rejects derived pages without source provenance and derivation metadata', () => {
  const result = validate({
    'records/source.md': completeSource,
    'records/derived.md': frontmatter(baseFields({ id: 'derived-fixture', type: 'derived' })),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /derived pages must declare at least one source_id/)
  assert.match(result.output, /derived\.method is required/)
})

test('rejects active derived pages', () => {
  const result = validate({
    'records/source.md': activeSource,
    'records/derived.md': completeDerived({ status: 'active' }),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /derived pages must have status draft/)
})

test('rejects active project-home pages', () => {
  const result = validate({
    'records/project-home.md': frontmatter(baseFields({
      id: 'active-project-home',
      type: 'project-home',
    }).replace('status: draft', 'status: active')),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /project-home pages must have status draft/)
})

test('rejects Markdown pages without the schema and confidentiality boundaries', () => {
  const result = validate({
    'records/page.md': frontmatter(`id: page-fixture
title: Fixture page
project: shared
type: reference
status: draft
canonical: false
owner: validator-test
created: 2026-08-20
updated: 2026-08-20
tags: [fixture]`),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /missing required field schema/)
  assert.match(result.output, /missing required field confidentiality/)
})

test('rejects related entries that do not resolve to a path-qualified page', () => {
  const result = validate({
    'records/page.md': frontmatter(baseFields({
      id: 'related-fixture',
      type: 'reference',
      extra: '\nrelated:\n  - records/missing-page',
    })),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /related target does not resolve: records\/missing-page/)
})

test('rejects project IDs outside the governed portfolio', () => {
  const fields = baseFields({ id: 'project-fixture', type: 'reference' })
    .replace('project: shared', 'project: unknown-project')
  const result = validate({
    'records/page.md': frontmatter(fields),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /frontmatter schema \/project must be equal to one of the allowed values/)
})

for (const classification of ['restricted', 'archive-only', 'superseded-candidate']) {
  test(`rejects source IDs backed by ${classification} Drive manifest records`, () => {
    const result = validate({
      'records/source.md': activeSource,
      'records/canon.md': frontmatter(baseFields({
        id: `canon-${classification}`,
        type: 'canon',
        extra: '\nsource_ids:\n  - src-fixture',
      })),
      'audit/manifests/fixture-drive-manifest-2026-08-20.jsonl': `${manifestRecord(classification)}\n`,
    })

    assert.notEqual(result.status, 0)
    assert.match(result.output, new RegExp(`excluded Drive manifest classification ${classification}`))
  })
}

test('rejects Telegram bot-token-shaped text without storing a usable credential', () => {
  const tokenShape = `${'12345'}:${'x'.repeat(35)}`
  const result = validate({
    'records/token.md': frontmatter(baseFields({ id: 'token-fixture', type: 'reference' }), `# Fixture\n\n${tokenShape}`),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /possible credential matched/)
})

test('rejects representative service-token-shaped text without storing usable credentials', () => {
  const tokenShapes = [
    `xoxb-${'x'.repeat(24)}`,
    `glpat-${'x'.repeat(24)}`,
    `sk_live_${'x'.repeat(24)}`,
  ]
  const result = validate({
    'records/tokens.md': frontmatter(baseFields({ id: 'tokens-fixture', type: 'reference' }), `# Fixture\n\n${tokenShapes.join('\n')}`),
  })

  assert.notEqual(result.status, 0)
  assert.match(result.output, /possible credential matched/)
})
