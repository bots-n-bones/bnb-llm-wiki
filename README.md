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
updated: 2026-08-19
tags: [knowledge-base, governance]
---

# Bots-n-bones Knowledge Base V2

This directory is the Git-backed knowledge layer for Hermes. Google Drive remains
the source of truth for original spreadsheets, documents, presentations, images,
video, and archival exports.

## Safety boundary

- The existing Google Drive tree is an immutable source during the pilot.
- No source file is moved, renamed, replaced, or deleted by KB V2 ingestion.
- Source records refer to originals by stable Google Drive file ID and URL.
- Generated text is stored under `90-derived/` and never overwrites a source.
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
`quntm`, `ursus`, and cross-project `shared` knowledge. Only SVMPX currently
has curated pilot evidence; every other project home is a non-canonical draft
placeholder until its sources are reviewed.
