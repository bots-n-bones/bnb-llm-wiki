---
schema: hermes-kb/v2
id: kb-bnb-case-registry-schema
title: Bots-n-Bones case registry schema
project: bots-n-bones
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Безопасная схема XLSX-реестра без выгрузки строк и рабочих значений.
aliases: [Колонки реестра кейсов, Схема XLSX Bots-n-Bones]
tags: [bots-n-bones, cases, spreadsheet, schema-only]
source_ids: [src-local-bnb-case-registry-dcea1f30]
derived:
  method: xlsx-structure-only
  generated_at: 2026-08-20T00:00:00Z
  extractor_version: manual-safe-audit-v1
created: 2026-08-20
updated: 2026-08-20
---

# Bots-n-Bones case registry schema

Книга содержит один видимый лист `Sheet1`. В первой строке обнаружены поля:
`Title`, `Comments 010625`, `Units`, `Tags`, `Product`, `Materials`,
`description file`, `design_md`, `Agents`; также присутствует заполненная
колонка K без установленного заголовка. Использованный диапазон — `A1:K30`
(30 строк × 11 колонок). Структурный анализ не обнаружил формул, поэтому
паттернов формул в книге нет. Значения строк не выгружены, и этот материал
нельзя использовать для подсчёта компаний или кейсов.

Evidence: [[projects/bots-n-bones/04-source-register/case-registry-xlsx]].
