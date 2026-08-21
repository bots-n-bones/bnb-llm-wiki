---
schema: hermes-kb/v2
id: kb-content-os-content-plan-workbook-schema
title: "Content OS content-plan workbook schema"
project: content-os
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [content-plan, xlsx-schema]
aliases:
  - "Структура XLSX шаблона контент-плана Content OS"
  - "Схема workbook content plan ContentOS"
  - "Поля таблицы контент-плана"
summary: "Какова структура XLSX-шаблона контент-плана Content OS: лист, диапазон, размеры, порядковые колонки и восемь строковых полей."
source_ids:
  - kb-content-os-source-content-plan-schema
derived:
  method: local-read-only-portfolio-curation
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Content OS content-plan workbook schema

## Workbook metadata

- Workbook: `IN _ Content-os _ Template content plan.xlsx`
- Sheet: `Sheet1`
- Used range: `A1:P9`
- Dimensions: 9 rows × 16 columns
- Structured Excel tables: none detected

## Layout schema

The top row is an ordinal series (`#`, 1–15). Row labels in the first column are: date, status, rubric, post idea, idea description, image format, text, and reference link.

## Privacy boundary

Only sheet/range dimensions and structural labels were retained. Dates and all per-post cell content were intentionally omitted.
