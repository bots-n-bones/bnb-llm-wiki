---
schema: hermes-kb/v2
id: kb-v2-root
title: Bots-n-bones Knowledge Base V2
type: index
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-19
updated: 2026-08-21
tags: [knowledge-base, governance]
---

# Bots-n-bones Knowledge Base V2

This directory is the Git-backed knowledge layer for Hermes. Google Drive remains
the source of truth for original spreadsheets, documents, presentations, images,
video, and archival exports.

## Safety boundary

- The existing Google Drive tree is an immutable source.
- No source file is moved, renamed, replaced, or deleted by KB V2 ingestion.
- Source records refer to originals by stable Google Drive file ID and URL.
- Generated text is first stored in private server staging. Approved drafts are
  added under the project knowledge tree and never overwrite a source.
- Canonical knowledge candidates are organized under `00-canon/`,
  `01-knowledge/`, `02-decisions/`, and `03-sops/`.
- Credentials and secrets are never copied into this repository.

## Layout

- `00-governance/` — metadata contract, lifecycle, and migration rules.
- `audit/` — immutable audit snapshots and duplicate reports.
- `projects/` — one canonical knowledge tree per project.
- `_templates/` — templates for repeatable knowledge records.

Each portfolio project uses the same layers: `00-canon/`, `01-knowledge/`,
`02-decisions/`, `03-sops/`, `04-source-register/`, `90-derived/`, and
`99-archive/`.

## Portfolio foundation

The portfolio contains `svmpx`, `hello-i-am`, `content-os`, `bots-n-bones`,
`quntm`, `ursus`, and cross-project `shared` knowledge. SVMPX has owner-approved
canon. Other projects contain registered evidence and non-canonical drafts that
remain in the owner review queue.

## Production flow

Hermes answers from a server-local, read-only SQLite FTS index. A read-only
Drive worker scans only the allowlisted `00 - inbox` folder every ten minutes,
uses stable Drive fingerprints, extracts bounded text where supported and
stores packages privately under `/opt/data/knowledge-intake`.

Publication is a separate gate. Ilya must explicitly approve an intake package;
only then can the release worker create a source record and a non-canonical
draft, validate the repository, push the revision and rebuild the SQLite index.
See [[00-governance/intake-operations|Knowledge Intake Operations]].
