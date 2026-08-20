---
schema: hermes-kb/v2
id: src-gdrive-175yflG6P0QmxAqTzalrCkTOs7LX8RKq8I8WuUMAgDxI
title: "SVMPX TG Chatbots"
project: svmpx
type: source-record
domain: bot-operations
status: active
canonical: false
owner: ilya
confidentiality: restricted
summary: "Legacy inventory of specialized Telegram bots and responsibilities; original contains secrets and must not be indexed as content."
aliases:
  - Telegram-боты с секретами
  - Источник с секретами вне KB
authority: restricted-inventory
tags: [svmpx, telegram, inventory, secrets, google-drive]
related:
  - "[[projects/svmpx/00-canon/bot-scenarios]]"
source:
  kind: google-drive
  drive_file_id: 175yflG6P0QmxAqTzalrCkTOs7LX8RKq8I8WuUMAgDxI
  url: https://docs.google.com/document/d/175yflG6P0QmxAqTzalrCkTOs7LX8RKq8I8WuUMAgDxI/edit
  parent_folder_id: 1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG
  original_path: "SVMPX/06_old_notion/SVMPX TG Chatbots"
  original_title: "SVMPX TG Chatbots"
  mime_type: application/vnd.google-apps.document
  created_time: 2026-06-06T07:14:07.534Z
  modified_time: 2026-06-06T07:14:09.245Z
  checksum: null
  revision_id: null
extraction:
  status: security-redacted-review
  method: connector-readable-text
  derived_path: null
dedupe:
  status: unreviewed
  exact_group: null
  preferred_source_id: null
created: 2026-08-19
updated: 2026-08-19
---

# SVMPX TG Chatbots

## Purpose

Records that the legacy environment contains specialized bots for notifications, proposals, product/offer search, statistics, and finance.

## Security boundary

The original contains secret material. Values are intentionally omitted, the source is not linked from the body, and its content must not be ingested into general search. Rotate exposed credentials and move them to a secret manager before integration.

## Authority

**restricted-inventory.** The inventory indicates historical or current bot identities, but runtime activity was not verified.

## Relationships

- [[projects/svmpx/00-canon/bot-scenarios]]
