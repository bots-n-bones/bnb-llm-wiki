---
schema: hermes-kb/v2
id: src-gdrive-1H8Ei74PQgrnQKcWBzJtoHoDZvRY1cBcW
title: "Purchase Order formation"
project: svmpx
type: source-record
domain: orders
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Procedure snapshot for forming and later updating a Purchase Order through Client Proposal."
authority: operational-guide-candidate
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-proposal-status-errors]]"
source:
  kind: google-drive
  drive_file_id: 1H8Ei74PQgrnQKcWBzJtoHoDZvRY1cBcW
  url: https://drive.google.com/file/d/1H8Ei74PQgrnQKcWBzJtoHoDZvRY1cBcW/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Как формируется PO.md"
  original_title: "Как формируется PO.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:34.216Z
  modified_time: 2026-05-17T11:31:33.000Z
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

# Purchase Order formation

[Open original on Google Drive](https://drive.google.com/file/d/1H8Ei74PQgrnQKcWBzJtoHoDZvRY1cBcW/view)

## Purpose

Describes how client quantities and supplier-agreed QTY Placed progress through CP into PO creation.

## Authority

**operational-guide-candidate.** Operational currency and accuracy must be verified against current behavior and approved by the owner. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-status-errors]]
