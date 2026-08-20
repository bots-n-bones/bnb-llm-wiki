---
schema: hermes-kb/v2
id: kb-v2-metadata-contract
title: KB V2 Metadata Contract
type: policy
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: [metadata, governance]
---

# KB V2 Metadata Contract

Every Markdown page must contain YAML frontmatter. IDs are stable and must not
be reused when a document is renamed or moved.

## Required fields

```yaml
---
id: kb-svmpx-example
title: Human-readable title
project: svmpx
type: canon
status: draft
canonical: false
owner: ilya
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: []
---
```

## Allowed values

- `type`: `index`, `canon`, `decision`, `sop`, `reference`, `research`,
  `source-record`, `derived`, `project-home`, `policy`.
- `status`: `draft`, `active`, `superseded`, `archived`, `quarantined`.
- `confidentiality`: `public`, `internal`, `restricted`.
- `canonical`: `true` only for a human-approved statement of current truth.

## Source block

Every source record carries complete original-artifact provenance:

```yaml
source:
  kind: google-drive
  drive_file_id: stable-file-id
  url: https://drive.google.com/...
  parent_folder_id: stable-parent-folder-id
  original_path: Original folder/source.md
  original_title: source.md
  mime_type: application/pdf
  modified_time: 2026-08-19T00:00:00Z
  checksum: null
  revision_id: null
```

If Google does not expose a checksum or revision for a native file, record that
field as `null`; folder, path, title, and modified time remain required.
Canonical and derived pages require non-empty `source_ids` that resolve to
source records. Derived pages also include:

```yaml
derived:
  method: extractor-name
  generated_at: 2026-08-20T00:00:00Z
  extractor_version: null
```

`related` is an optional, unique array of project-path or path-qualified wiki
links. `provenance` is an optional structured extension for capture method,
capture time, and source IDs; it does not replace the required source contract.
`confidentiality` is required on every page.

## Links

Hermes now consumes `related` for graph edges and backlinks. Important
relationships must still appear as body wiki links so they remain visible to
humans, work in older clients, and pass repository link validation.
