---
schema: hermes-kb/v2
id: src-gdrive-16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh
title: "Shipments overview"
project: svmpx
type: source-record
domain: logistics
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Overview of Shipment purpose, timeline, dates, quantities, filters, and progress."
authority: conceptual-operational-reference
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/shipment-in-create]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipment-out-create]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]"
source:
  kind: google-drive
  drive_file_id: 16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh
  url: https://drive.google.com/file/d/16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Что такое shipments.md"
  original_title: "Что такое shipments.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:34.632Z
  modified_time: 2026-05-17T11:33:30.000Z
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

# Shipments overview

[Open original on Google Drive](https://drive.google.com/file/d/16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh/view)

## Purpose

Explains Shipments as the layer for real inbound and outbound movement against Purchase Orders.

## Authority

**conceptual-operational-reference.** Operational currency and accuracy must be verified against current behavior and approved by the owner. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/shipment-in-create]]
- [[projects/svmpx/04-source-register/sources/documentation/shipment-out-create]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]
