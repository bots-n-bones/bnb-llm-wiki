---
schema: hermes-kb/v2
id: src-gdrive-1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4
title: SVMPX System Documentation Map
project: svmpx
type: source-record
domain: system
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: Source map and proposed outline for SVMPX system documentation, including known conflicts requiring review.
tags: [svmpx, system, architecture, data-model]
source:
  kind: google-drive
  drive_file_id: 1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4
  url: https://docs.google.com/document/d/1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: 06_old_notion/SVMPX System Documentation Map
  original_title: SVMPX System Documentation Map
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:09:59.696Z
  modified_time: 2026-06-06T07:10:01.532Z
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

# SVMPX System Documentation Map

[Open original on Google Drive](https://docs.google.com/document/d/1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4/edit)

## Purpose

Proposes the target system document: architecture, entities, processes, file
formats, imports, bot behavior, integrations, security, operations, and QA.

## Known review items

- Date format is inconsistent across sources.
- The business distinction between `PO` and `ORD` must be approved.
- File naming conventions differ from observed Telegram files.
- The future boundary between Airtable UI and Telegram bot is unresolved.

These conflicts make this a canonical candidate source, not a canonical page.

## Relationships

- [[projects/svmpx/04-source-register/sources/master-index|Legacy master index]]
- [[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion full export map]]
