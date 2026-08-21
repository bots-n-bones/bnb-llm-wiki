---
schema: hermes-kb/v2
id: src-local-bnb-project-manifest
title: BnB downloaded project local manifest
project: svmpx
type: source-record
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Read-only SHA-256 inventory of all downloaded BnB project fragments; values from spreadsheets and archives are not copied into the Wiki.
tags: [svmpx, source, local-source, manifest, attachments, deduplication]
source:
  kind: local-directory-manifest
  drive_file_id: local:bnb-project:manifest
  url: local://bnb-project/manifest
  mime_type: application/x-ndjson
  parent_folder_id: local:bnb-project
  original_path: knowledge-v2/audit/local/bnb-local-manifest.jsonl
  original_title: bnb-local-manifest.jsonl
  modified_time: 2026-08-21T02:20:20Z
  checksum: 0c3a4ff7180550cc24983f36adb1dbd2a2022b73f930d19ffa90da7984ebe090
  revision_id: sha256:0c3a4ff7180550cc24983f36adb1dbd2a2022b73f930d19ffa90da7984ebe090
created: 2026-08-21
updated: 2026-08-21
---

# BnB downloaded project local manifest

The manifest registers 11,854 local files without changing the downloaded
source tree. Each record preserves the original path, absolute local path,
MIME, size, modified time, SHA-256, duplicate group, safety classification and
deterministic preferred candidate.

SVMPX accounts for 2,873 records and 907,385,653 bytes across three downloaded
fragments. Exact duplicate candidates are excluded from normal attachment
lookup. Archives were hashed but never extracted. Spreadsheet values were not
copied into this source record.

The machine inventory is stored in `audit/local/bnb-local-manifest.jsonl`; exact
duplicate groups and the read-only audit summary are stored beside it.
