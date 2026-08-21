---
schema: hermes-kb/v2
id: src-gdrive-1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo
title: SVMPX Notion Full Export Map
project: svmpx
type: source-record
domain: sources
status: active
canonical: false
owner: ilya
confidentiality: restricted
summary: Карта полного экспорта Notion, включая ограниченные источники с секретами, которые запрещено переносить в KB.
aliases:
  - Карта экспорта Notion
tags: [svmpx, notion, export, inventory]
source:
  kind: google-drive
  drive_file_id: 1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo
  url: https://docs.google.com/document/d/1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: 06_old_notion/SVMPX Notion Full Export Map
  original_title: SVMPX Notion Full Export Map
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:09:39.541Z
  modified_time: 2026-06-06T07:09:41.599Z
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
classification: archive-only
---

# SVMPX Notion Full Export Map

[Open original on Google Drive](https://docs.google.com/document/d/1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo/edit)

## Purpose

Inventories a roughly 44 MB Notion export containing 61 Markdown pages, 74 PNG,
7 MP4, and several structured or web formats. It separates core logistics pages,
technical infrastructure, and unrelated content-factory material.

## Proposed canonical outputs

- Project and system documentation.
- Data model.
- Bot scenarios and messages.
- DDP and finance flow.
- QA protocol.
- Roadmap.

## Safety signal

The map identifies a credentials page that must remain an original restricted
source and must not be copied into KB V2.

The package is classified `archive-only`; individually reviewed pages may be
registered as supporting sources. Restricted credential pages remain excluded.

## Relationships

- [[projects/svmpx/04-source-register/sources/source-register|Legacy source register]]
- [[projects/svmpx/04-source-register/sources/system-documentation-map|System documentation map]]
