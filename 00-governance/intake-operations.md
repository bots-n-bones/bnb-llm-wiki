---
schema: hermes-kb/v2
id: kb-v2-intake-operations
title: Knowledge Intake Operations
project: shared
type: sop
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Production commands and gates for Drive Inbox and Hermes message ingestion.
created: 2026-08-21
updated: 2026-08-21
tags: [inbox, drive, ingestion, release, rollback]
---

# Knowledge Intake Operations

## Automated scan

Every ten minutes the VPS runs the read-only Drive intake worker against the
canonical `00 - inbox` folder. It recursively inventories direct descendants,
compares Drive fingerprints and stages only new or changed files. Documents,
PDF, DOCX, PPTX and XLSX receive bounded text extraction; media receives a
metadata-only record.

Private runtime state lives at `/opt/data/knowledge-intake`:

- `manifest.jsonl` and checksums — latest complete Inbox snapshot;
- `state.json` — incremental cursor by Drive file ID;
- `pending/*.json` — private review packages;
- `runs/*.json` and `health.json` — receipts and health state.

## Hermes commands

Hermes uses these commands through the `bnb-knowledge` skill:

```bash
python3 /opt/knowledge/bnb-llm-wiki/scripts/manage-intake.py list \
  --staging /opt/data/knowledge-intake

python3 /opt/knowledge/bnb-llm-wiki/scripts/manage-intake.py stage-note \
  --staging /opt/data/knowledge-intake --project shared \
  --title "Title" --text "User-approved note"
```

Explicit owner approval is recorded with:

```bash
python3 /opt/knowledge/bnb-llm-wiki/scripts/manage-intake.py approve \
  --staging /opt/data/knowledge-intake --id INTAKE_ID --by ilya
```

Approval permits publication of a source record and draft; it does not permit
canonical promotion. Rejection records a review note and keeps the original
Drive object untouched.

## Release and rollback

The host publisher notices approved packages, materializes source records plus
`canonical: false` drafts, runs repository validation and pushes a Git revision.
The release worker then rebuilds SQLite and performs a retrieval smoke test.
If any release step fails, the deployment clone and database are restored to
their previous known-good versions.
