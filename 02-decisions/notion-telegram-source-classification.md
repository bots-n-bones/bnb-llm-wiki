---
schema: hermes-kb/v2
id: decision-notion-telegram-source-classification
title: Notion and Telegram Source Classification
project: svmpx
type: decision
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Classification boundary for legacy Notion exports and Telegram materials in KB V2.
source_ids: [src-gdrive-112adjNbytFfsySWqLvakrHzSewScupwsRVNyArBCsv4, src-gdrive-1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo]
created: 2026-08-21
updated: 2026-08-21
tags: [notion, telegram, classification, security, archive]
---

# Notion and Telegram Source Classification

## Decision

- The legacy Notion full export is `archive-only` as a package and
  `supporting-source` for individually registered, reviewed pages.
- Credential-bearing Notion pages are `restricted`; their content is excluded
  from general extraction, Git and normal search.
- Raw Telegram chat exports are `archive-only` and out of scope for automatic
  V1 ingestion. They may be consulted only through an explicit, authorized
  review task.
- Reviewed Telegram bot copy may remain supporting evidence for UX and bot
  scenarios, but it does not prove current runtime behavior.
- Telegram inventories containing tokens, bot secrets or credentials are
  `restricted` and metadata-only. Secret values must never enter the Wiki.

This classification preserves the original Drive artifacts and does not delete,
move or rewrite any export.

## Promotion boundary

A fact from these sources becomes canonical only after it is separated from
secrets, linked to a registered source, checked against current production and
explicitly approved by the owner.
