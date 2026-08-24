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
updated: 2026-08-24
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

## Post-canonical Drive housekeeping

Drive intake remains read-only through extraction, drafting, review, and the
canonical Git release. After the canonical release and index refresh have
completed successfully, a separate worker may move the original Drive file:

- the intake must have `status: published-canonical` and a stable
  `drive_file_id`;
- the current file parent must be inside canonical `00 - inbox`;
- the destination must be an explicitly reviewed project-folder ID under the
  canonical `01 - projects` folder;
- ambiguous, missing, out-of-root, trashed, or multi-parent sources are blocked
  without mutation;
- the source record keeps its original path, Drive file ID, checksum, revision,
  and stable Drive URL as historical provenance;
- the move receipt is stored privately in the intake package under
  `drive_move`; failures never roll back the canonical release.

`scripts/move-published-drive-intake.py` performs the mutation independently.
`config/drive-project-destinations.json` is the reviewed allowlist. Projects
without an unambiguous destination remain disabled until owner review.
