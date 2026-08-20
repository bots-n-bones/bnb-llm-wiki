---
schema: hermes-kb/v2
id: src-gdrive-1lDvVIA19MTx1WRzt2rRyJTTq_r0ofODJ
title: "Create Shipment OUT"
project: svmpx
type: source-record
domain: logistics
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Procedure snapshot for outbound Shipment creation and control ratios."
authority: operational-guide-candidate
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]"
source:
  kind: google-drive
  drive_file_id: 1lDvVIA19MTx1WRzt2rRyJTTq_r0ofODJ
  url: https://drive.google.com/file/d/1lDvVIA19MTx1WRzt2rRyJTTq_r0ofODJ/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Как создать shipment out.md"
  original_title: "Как создать shipment out.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:34.211Z
  modified_time: 2026-05-17T11:34:02.000Z
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

# Create Shipment OUT

[Open original on Google Drive](https://drive.google.com/file/d/1lDvVIA19MTx1WRzt2rRyJTTq_r0ofODJ/view)

## Purpose

Describes creation of outbound delivery from a PO, required dates and quantities, and execution stages.

## Authority

**operational-guide-candidate.** Operational currency and accuracy must be verified against current behavior and approved by the owner. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]
