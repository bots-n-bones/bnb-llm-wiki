---
schema: hermes-kb/v2
id: src-gdrive-15UhPB1FCOp-bs6GK_tLX27wOLMl-V-90
title: "Product statuses and errors"
project: svmpx
type: source-record
domain: product-data
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Reference for product lifecycle and data-quality states affecting downstream eligibility."
authority: operational-rules-candidate
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/products-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/products-upload-delete]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/product-card]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/source-offers-status-errors]]"
source:
  kind: google-drive
  drive_file_id: 15UhPB1FCOp-bs6GK_tLX27wOLMl-V-90
  url: https://drive.google.com/file/d/15UhPB1FCOp-bs6GK_tLX27wOLMl-V-90/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Какие есть статусы и ошибки.md"
  original_title: "Какие есть статусы и ошибки.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:36.361Z
  modified_time: 2026-05-17T11:28:27.000Z
  checksum: null
  revision_id: null
extraction:
  status: metadata-reviewed
  method: connector-readable-text
  derived_path: null
dedupe:
  status: unreviewed
  exact_group: null
  preferred_source_id: null
created: 2026-08-19
updated: 2026-08-19
---

# Product statuses and errors

[Open original on Google Drive](https://drive.google.com/file/d/15UhPB1FCOp-bs6GK_tLX27wOLMl-V-90/view)

## Purpose

Records working and automatic product states, including duplicate and invalid-category remediation.

## Authority

**operational-rules-candidate.** Operational currency and accuracy must be verified against current behavior and approved by the owner. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/products-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/products-upload-delete]]
- [[projects/svmpx/04-source-register/sources/documentation/product-card]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-status-errors]]
