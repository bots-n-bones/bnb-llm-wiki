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
updated: 2026-08-24
tags: [knowledge-base, governance]
---

# Bots-n-bones Knowledge Base V2

This directory is the Git-backed knowledge layer for Hermes. Google Drive remains
the source of truth for original spreadsheets, documents, presentations, images,
video, and archival exports.

## Safety boundary

- Google Drive is read-only during inventory, extraction, review, and drafting.
- A narrow post-publication worker may move an original file only after its
  intake is successfully published as canonical, only from governed `00 - inbox`
  scope to an allowlisted project folder under the canonical Drive root.
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
`quntm`, `ursus`, `hermes`, and cross-project `shared` knowledge. SVMPX has owner-approved
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
After a later owner-approved canonical release succeeds, Drive housekeeping is
queued independently. A move failure is recorded in private intake state and
cannot roll back or invalidate the published canonical revision.
See [[00-governance/intake-operations|Knowledge Intake Operations]].
