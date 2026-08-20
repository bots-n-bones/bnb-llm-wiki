---
schema: hermes-kb/v2
id: kb-hello-i-am-collaboration-database-schema
title: "Hello I Am collaborations workbook schema"
project: hello-i-am
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [collaborations, xlsx-schema]
aliases:
  - "Поля workbook базы коллабораций Hello I Am"
  - "Схема XLSX базы партнёров Hello I Am"
  - "Колонки базы collaborations"
summary: "Какие поля есть в workbook базы коллабораций Hello I Am: схема листа, диапазон, размеры и названия 13 колонок без строк контактов."
source_ids:
  - kb-hello-i-am-source-collabs-database-schema
derived:
  method: local-read-only-portfolio-curation
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Hello I Am collaborations workbook schema

## Workbook metadata

- Workbook: `Data Base.xlsx`
- Sheet: `Лист1`
- Used range: `A1:M67`
- Dimensions: 67 rows × 13 columns
- Structured Excel tables: none detected

## Header schema

`name`, `platform`, `username`, `link`, `location`, `language`, `core audience`, `subscribers`, `actions`, `ER (actions/subscribers, %)`, `type`, `familiar`, `connection status`.

## Privacy boundary

Only workbook structure and the header row were captured. Contact rows, usernames, links, metrics, and other cell values were not copied into the knowledge base.
