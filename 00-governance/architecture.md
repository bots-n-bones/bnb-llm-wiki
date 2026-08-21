---
schema: hermes-kb/v2
id: kb-v2-architecture
title: KB V2 Architecture
type: decision
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Separation of canonical Markdown, readonly Drive sources, private intake staging, derived representations, and the Hermes materialized index.
created: 2026-08-19
updated: 2026-08-21
tags: [architecture, ingestion, search, google-drive]
---

# KB V2 Architecture

## Decision

KB V2 uses four explicit layers:

1. Governed Markdown in the public `bots-n-bones/bnb-llm-wiki` Git repository.
2. Original artifacts on Google Drive, accessed read-only.
3. Private server staging for unapproved extracts and review decisions.
4. Reproducible derived Markdown generated from approved sources.
5. A local materialized index used by Hermes UI and agents.

There is no bidirectional synchronization and no automated Drive-to-canonical
overwrite.

## Data flow

```text
Git canonical Markdown ───────────────┐
                                      ├─> materialized index ─> Hermes
Drive Inbox -> private staging -> approval -> source records ─┤
                                      -> derived drafts ──────┘
```

## Production integration

The GitHub Wiki is version history and the server checkout is a deployment
artifact. Hermes never answers by downloading Drive files on demand. The
server refreshes validated Git revisions, atomically rebuilds SQLite and keeps
the previous database for rollback.

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
3. Spreadsheet text and bounded row extracts.
4. Media metadata only; OCR and transcription require a separate approved job.

## Operational guarantees

- Drive access is OAuth `drive.readonly` and restricted to an allowlisted root.
- Unapproved extracts remain outside the public Git repository.
- Generated drafts are always `canonical: false`.
- Published SQLite is atomically replaced with mode `0644` and verified from
  the unprivileged Hermes account.
- A failed release restores the previous Git revision and SQLite database.

See [[00-governance/metadata-contract|KB V2 Metadata Contract]] and
[[00-governance/lifecycle|KB V2 Lifecycle and Rollback]].
