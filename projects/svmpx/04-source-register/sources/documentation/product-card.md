---
schema: hermes-kb/v2
id: src-gdrive-1Zp57yQSa9pPbzY4AjWYsVdhHqT_3hzte
title: "Product card"
project: svmpx
type: source-record
domain: product-data
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Time-sensitive interface snapshot for Product card fields and offer analytics."
authority: interface-snapshot
tags: [svmpx, documentation, google-drive]
related:
  - "[[projects/svmpx/04-source-register/sources/documentation/products-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/products-upload-delete]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/products-status-errors]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/source-offers-card]]"
source:
  kind: google-drive
  drive_file_id: 1Zp57yQSa9pPbzY4AjWYsVdhHqT_3hzte
  url: https://drive.google.com/file/d/1Zp57yQSa9pPbzY4AjWYsVdhHqT_3hzte/view
  parent_folder_id: 1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n
  original_path: "01_documentation/Из чего состоит карточка продукта.md"
  original_title: "Из чего состоит карточка продукта.md"
  mime_type: text/markdown
  created_time: 2026-06-05T11:38:34.279Z
  modified_time: 2026-05-17T11:28:19.000Z
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

# Product card

[Open original on Google Drive](https://drive.google.com/file/d/1Zp57yQSa9pPbzY4AjWYsVdhHqT_3hzte/view)

## Purpose

Maps General, Details, EXW & Offers, and metadata to identity, inherited parameters, analytics, and archive actions.

## Authority

**interface-snapshot.** UI labels and behavior must be visually verified against the current product. This source record is not canonical and does not reproduce the source text.

## Relationships

- [[projects/svmpx/04-source-register/sources/documentation/products-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/products-upload-delete]]
- [[projects/svmpx/04-source-register/sources/documentation/products-status-errors]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-card]]
