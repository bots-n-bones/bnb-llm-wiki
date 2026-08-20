---
schema: hermes-kb/v2
id: kb-v2-architecture
title: KB V2 Architecture
type: decision
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Separation of canonical Markdown, readonly Drive sources, derived representations, and the Hermes materialized index.
created: 2026-08-19
updated: 2026-08-19
tags: [architecture, ingestion, search, google-drive]
---

# KB V2 Architecture

## Decision

KB V2 uses four explicit layers:

1. Canonical Markdown in the private `bots-n-bones-kb` Git repository.
2. Original artifacts on Google Drive, accessed read-only.
3. Reproducible derived Markdown generated from selected sources.
4. A local materialized index used by Hermes UI and agents.

There is no bidirectional synchronization and no automated Drive-to-canonical
overwrite.

## Data flow

```text
Git canonical Markdown ───────────────┐
                                      ├─> materialized index ─> Hermes
Drive originals -> source records ────┤
                -> derived Markdown ──┘
```

## Pilot integration

The KB repository is private. The current Hermes GitHub provider has no private
repository authentication, so the SVMPX pilot uses a local checkout as its
knowledge source. Private GitHub support is a separate implementation gate.

## Index MVP

- SQLite manifest and FTS5 search.
- Stable document IDs independent of paths.
- Canonical results rank above source records and derived text.
- Filters for project, layer, type, status, and confidentiality.
- Graph edges from explicit links, source relationships, and derived-from
  relationships.
- Embeddings are deferred until FTS quality and confidentiality controls are
  measured.

## Drive ingestion contract

- Allowlisted root folder IDs only.
- Read/list/export/download operations only.
- Identity by Drive file ID; rename or move does not create a new source.
- Incremental fingerprint from revision/version, modified time, checksum, and
  extractor version.
- Failed extraction does not advance the synchronization cursor.
- Missing files become tombstones in the index; Drive objects are not deleted.

## Extraction priority

1. Existing Markdown and Google Docs.
2. PDF and DOCX.
3. Spreadsheet schema and bounded summaries, not full cell dumps.
4. OCR and media transcription after the document pilot.

## Known Hermes gaps

- GitHub cache materialization can flatten nested paths and does not clean stale
  files atomically.
- Private GitHub authentication is absent.
- Search still rereads the full corpus for every request; Unicode word-boundary
  handling is implemented, but indexing is not.
- Graph identity is currently the file path rather than stable frontmatter ID.
- Frontmatter relationships are parsed for the in-memory graph, but are not yet
  persisted in a materialized index.
- Long synchronization runs are synchronous HTTP requests.

See [[00-governance/metadata-contract|KB V2 Metadata Contract]] and
[[00-governance/lifecycle|KB V2 Lifecycle and Rollback]].
