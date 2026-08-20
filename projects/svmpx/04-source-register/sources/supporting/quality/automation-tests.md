---
schema: hermes-kb/v2
id: src-gdrive-1ImiLnOXLysLgprKDYZhvVbiqQp2n3UP4kdHWYcfcH88
title: SVMPX Automation Tests
project: svmpx
type: source-record
domain: quality
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: "Legacy checklist claiming completion of ingestion, proposal, notification, parsing, and Airtable automations."
tags: [svmpx, source, qa, automation]
source:
  kind: google-drive
  drive_file_id: 1ImiLnOXLysLgprKDYZhvVbiqQp2n3UP4kdHWYcfcH88
  url: https://docs.google.com/document/d/1ImiLnOXLysLgprKDYZhvVbiqQp2n3UP4kdHWYcfcH88/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: "06_old_notion/SVMPX Automation Tests"
  original_title: "SVMPX Automation Tests"
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:14:16.926Z
  modified_time: 2026-06-06T07:14:18.555Z
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

# SVMPX Automation Tests

[Open original on Google Drive](https://docs.google.com/document/d/1ImiLnOXLysLgprKDYZhvVbiqQp2n3UP4kdHWYcfcH88/edit)

## Confirmed content

The source marks checklist items as completed for product and offer ingestion,
proposal comments and email delivery, notifications and logging, parsing, and
several Airtable automations. The min/max/average product update is explicitly
described as no longer needed. An `AI` heading contains no documented checks.

## Evidence limitation

The checklist does not identify the tested environment, build, execution date,
fixtures, logs, failures, or current implementation status. Its checkmarks are
historical claims and must not be treated as a current passing run.

## Relationships

- [[projects/svmpx/00-canon/qa-protocol|Draft QA protocol]]
- [[projects/svmpx/00-canon/system-documentation|Draft system documentation]]
