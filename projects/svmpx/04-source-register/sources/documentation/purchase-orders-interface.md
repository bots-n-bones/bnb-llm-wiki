---
schema: hermes-kb/v2
id: src-gdrive-1wL-K24aO0CxQgRKvu7Upn4OpvMYcvNFK
title: "Purchase Orders interface overview"
project: svmpx
type: source-record
domain: orders
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Time-sensitive interface snapshot for Purchase Order list and detail views."
authority: interface-snapshot
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-orders-status-errors]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]"
source:
  kind: google-drive
  drive_file_id: 1wL-K24aO0CxQgRKvu7Upn4OpvMYcvNFK
  url: https://drive.google.com/file/d/1wL-K24aO0CxQgRKvu7Upn4OpvMYcvNFK/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Обзор интерфейсов заказов.md"
  original_title: "Обзор интерфейсов заказов.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:36.211Z
  modified_time: 2026-05-17T11:32:58.000Z
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

# Purchase Orders interface overview

[Open original on Google Drive](https://drive.google.com/file/d/1wL-K24aO0CxQgRKvu7Upn4OpvMYcvNFK/view)

## Purpose

Maps the PO Kanban and card tabs to status, quantity, money, warning, and date monitoring.

## Authority

**interface-snapshot.** UI labels and behavior must be visually verified against the current product. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-orders-status-errors]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]
