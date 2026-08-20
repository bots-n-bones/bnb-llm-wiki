---
schema: hermes-kb/v2
id: src-gdrive-112adjNbytFfsySWqLvakrHzSewScupwsRVNyArBCsv4
title: SVMPX Legacy Source Register
project: svmpx
type: source-record
domain: sources
status: active
canonical: false
owner: ilya
confidentiality: restricted
summary: Existing register for Telegram and Notion source packages and provenance rules.
tags: [svmpx, provenance, telegram, notion]
source:
  kind: google-drive
  drive_file_id: 112adjNbytFfsySWqLvakrHzSewScupwsRVNyArBCsv4
  url: https://docs.google.com/document/d/112adjNbytFfsySWqLvakrHzSewScupwsRVNyArBCsv4/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: 06_old_notion/SVMPX Source Register
  original_title: SVMPX Source Register
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:09:26.808Z
  modified_time: 2026-06-06T07:09:28.975Z
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

# SVMPX Legacy Source Register

[Open original on Google Drive](https://docs.google.com/document/d/112adjNbytFfsySWqLvakrHzSewScupwsRVNyArBCsv4/edit)

## Purpose

Registers Telegram Clothing/Electronics chat exports and the Notion SVMPX export.
It already defines provenance rules for facts from chats and Notion pages.

## Safety signal

The source explicitly says credentials pages must not be transferred into the
open knowledge base. KB V2 preserves that rule and treats this source as
`restricted` until its references are reviewed.

## Relationships

- [[projects/svmpx/04-source-register/README|SVMPX Source Register]]
- [[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion full export map]]
