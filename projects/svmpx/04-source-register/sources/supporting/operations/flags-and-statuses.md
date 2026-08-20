---
schema: hermes-kb/v2
id: src-gdrive-1OhNpOFjyqWciHOKPJ83Zn_Nqk-svpg04de856oVR92s
title: "SVMPX Flags and Statuses"
project: svmpx
type: source-record
domain: bot-operations
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Detailed Brutto interaction states, validation messages, status labels, logging requirements, and test cases."
authority: operational-rules-candidate
tags: [svmpx, telegram, brutto, statuses, google-drive]
related:
  - "[[projects/svmpx/00-canon/bot-scenarios]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/bot-brutto-scenarios]]"
source:
  kind: google-drive
  drive_file_id: 1OhNpOFjyqWciHOKPJ83Zn_Nqk-svpg04de856oVR92s
  url: https://docs.google.com/document/d/1OhNpOFjyqWciHOKPJ83Zn_Nqk-svpg04de856oVR92s/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: "SVMPX/06_old_notion/SVMPX Flags and Statuses"
  original_title: "SVMPX Flags and Statuses"
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:13:08.750Z
  modified_time: 2026-06-06T07:13:10.568Z
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

# SVMPX Flags and Statuses

[Open original on Google Drive](https://docs.google.com/document/d/1OhNpOFjyqWciHOKPJ83Zn_Nqk-svpg04de856oVR92s/edit)

## Purpose

Provides the most detailed operating copy for Brutto, including state fields, file rules, expected results, error handling, audit logs, and minimum scenario tests.

## Authority

**operational-rules-candidate.** Terms and state names require reconciliation with the deployed bot and Airtable schema.

## Relationships

- [[projects/svmpx/00-canon/bot-scenarios]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/bot-brutto-scenarios]]
