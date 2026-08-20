---
schema: hermes-kb/v2
id: src-gdrive-1qz5Kmq2mJa2TE4ICejJr7gaMjH5VvmF_
title: "Purchase Order statuses and errors"
project: svmpx
type: source-record
domain: orders
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Reference for Purchase Order lifecycle, warnings, and problem scenarios."
authority: operational-rules-candidate
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-orders-interface]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors]]"
source:
  kind: google-drive
  drive_file_id: 1qz5Kmq2mJa2TE4ICejJr7gaMjH5VvmF_
  url: https://drive.google.com/file/d/1qz5Kmq2mJa2TE4ICejJr7gaMjH5VvmF_/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Какие есть статусы и ошибки заказы.md"
  original_title: "Какие есть статусы и ошибки заказы.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:34.126Z
  modified_time: 2026-05-17T11:33:13.000Z
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

# Purchase Order statuses and errors

[Open original on Google Drive](https://drive.google.com/file/d/1qz5Kmq2mJa2TE4ICejJr7gaMjH5VvmF_/view)

## Purpose

Records PO statuses aggregated from Shipments, warnings, and incomplete or inconsistent execution cases.

## Authority

**operational-rules-candidate.** Operational currency and accuracy must be verified against current behavior and approved by the owner. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-orders-interface]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors]]
