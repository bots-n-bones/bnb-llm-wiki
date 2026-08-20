---
schema: hermes-kb/v2
id: src-gdrive-1OR6h15u1TEFm7ijB1IbsjzEzhRrVao51
title: "Shipment statuses and errors"
project: svmpx
type: source-record
domain: logistics
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Shipment status and validation reference covering Draft through closure and common logistics inconsistencies."
authority: operational-rules-candidate
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipment-in-create]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipment-out-create]]"
source:
  kind: google-drive
  drive_file_id: 1OR6h15u1TEFm7ijB1IbsjzEzhRrVao51
  url: https://drive.google.com/file/d/1OR6h15u1TEFm7ijB1IbsjzEzhRrVao51/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Какие есть статусы и ошикби shipment.md"
  original_title: "Какие есть статусы и ошикби shipment.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:34.517Z
  modified_time: 2026-05-17T11:34:21.000Z
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

# Shipment statuses and errors

[Open original on Google Drive](https://drive.google.com/file/d/1OR6h15u1TEFm7ijB1IbsjzEzhRrVao51/view)

## Purpose

Records Shipment lifecycle states and common quantity, sequence, and required-field errors.

## Authority

**operational-rules-candidate.** Operational currency and accuracy must be verified against current behavior and approved by the owner. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/shipment-in-create]]
- [[projects/svmpx/04-source-register/sources/documentation/shipment-out-create]]
