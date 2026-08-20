---
schema: hermes-kb/v2
id: src-gdrive-1yNDuuMrH7e-iUlXTudIY8mMZivugPI9w2n1tfI_lUN8
title: "SVMPX Bot Brutto Scenarios"
project: svmpx
type: source-record
domain: bot-operations
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Scenario specification for Brutto imports, commands, validations, responses, and logistics actions."
authority: operational-specification-candidate
tags: [svmpx, telegram, brutto, operations, google-drive]
related:
  - "[[projects/svmpx/00-canon/bot-scenarios]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/flags-and-statuses]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/chatbots-messages]]"
source:
  kind: google-drive
  drive_file_id: 1yNDuuMrH7e-iUlXTudIY8mMZivugPI9w2n1tfI_lUN8
  url: https://docs.google.com/document/d/1yNDuuMrH7e-iUlXTudIY8mMZivugPI9w2n1tfI_lUN8/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: "SVMPX/06_old_notion/SVMPX Bot Brutto Scenarios"
  original_title: "SVMPX Bot Brutto Scenarios"
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:10:27.391Z
  modified_time: 2026-06-06T07:10:28.630Z
  checksum: null
  revision_id: null
extraction:
  status: content-reviewed
  method: connector-readable-text
  derived_path: null
dedupe:
  status: unreviewed
  exact_group: null
  preferred_source_id: null
created: 2026-08-19
updated: 2026-08-19
---

# SVMPX Bot Brutto Scenarios

[Open original on Google Drive](https://docs.google.com/document/d/1yNDuuMrH7e-iUlXTudIY8mMZivugPI9w2n1tfI_lUN8/edit)

## Purpose

Defines the intended Brutto menu, file-import cycle, validation rules, commands, operational responses, and minimum tests across SO, PrePO, ORD/PO, Inbound, Outbound, Received, and discrepancy flows.

## Authority

**operational-specification-candidate.** The document describes intended behavior; production implementation was not verified during this read-only review.

## Relationships

- [[projects/svmpx/00-canon/bot-scenarios]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/flags-and-statuses]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/chatbots-messages]]
