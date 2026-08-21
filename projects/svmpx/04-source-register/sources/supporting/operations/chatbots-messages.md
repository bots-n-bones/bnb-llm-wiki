---
schema: hermes-kb/v2
id: src-gdrive-1TZTe8Md7BFdRswSk0JRT2kYUN1nh5r2fHq8_uTEtkkI
title: "SVMPX Chatbots Messages"
project: svmpx
type: source-record
domain: bot-operations
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Brutto tone, message structure, entity terminology, templates, success/error copy, and user paths."
authority: content-and-ux-candidate
tags: [svmpx, telegram, brutto, ux-writing, google-drive]
related:
  - "[[projects/svmpx/00-canon/bot-scenarios]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/bot-brutto-scenarios]]"
source:
  kind: google-drive
  drive_file_id: 1TZTe8Md7BFdRswSk0JRT2kYUN1nh5r2fHq8_uTEtkkI
  url: https://docs.google.com/document/d/1TZTe8Md7BFdRswSk0JRT2kYUN1nh5r2fHq8_uTEtkkI/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: "SVMPX/06_old_notion/SVMPX Chatbots Messages"
  original_title: "SVMPX Chatbots Messages"
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:13:35.290Z
  modified_time: 2026-06-06T07:13:36.658Z
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
classification: supporting-source
---

# SVMPX Chatbots Messages

[Open original on Google Drive](https://docs.google.com/document/d/1TZTe8Md7BFdRswSk0JRT2kYUN1nh5r2fHq8_uTEtkkI/edit)

## Purpose

Defines Brutto tone and microcopy and provides message variants for SO, PrePO, ORD, shipment, receipt, and discrepancy scenarios.

## Authority

**content-and-ux-candidate.** Copy and entity names require alignment with the final state machine and production labels.

The reviewed copy is supporting evidence; raw Telegram exports remain
`archive-only` and outside automatic V1 ingestion.

## Relationships

- [[projects/svmpx/00-canon/bot-scenarios]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/bot-brutto-scenarios]]
