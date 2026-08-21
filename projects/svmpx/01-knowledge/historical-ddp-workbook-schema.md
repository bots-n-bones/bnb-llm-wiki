---
schema: hermes-kb/v2
id: kb-svmpx-historical-ddp-workbook-schema
title: Historical SVMPX DDP workbook fields
project: svmpx
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Поля исторической DDP-книги и границы их безопасного использования.
aliases: [SDA master, Поля DDP таблицы, Исторический расчёт DDP]
tags: [svmpx, ddp, finance, spreadsheet, historical]
source_ids: [src-gdrive-11SnMFpVevWV8OwlXYQau-meyUpay9KQP]
derived:
  method: bounded-spreadsheet-text-extraction
  generated_at: 2026-08-21T00:00:00Z
  extractor_version: google-drive-readonly-v1
created: 2026-08-21
updated: 2026-08-21
---

# Historical SVMPX DDP workbook fields

> Historical evidence only. This page is not an executable calculator.

The workbook exposes a useful field sequence: EXW and currency; Serbian
markup; delivery region; pallet logistics and totals; tariff; `DAP + Tariff`;
VAT; `DDP`; Russian markup; final price and market-comparison values. Its
parameter area also names pallet capacity, FCL cost, FCL pallet cost, LCL
one-pallet cost and a step value.

This corroborates the high-level chain in
[[projects/svmpx/00-canon/ddp-finance-flow]], but does not resolve its open
ambiguities: formula grouping, units, current status of LC-001, and which
inputs are currently maintained in Airtable. Therefore no numerical result
may be represented as current canon from this workbook alone.

Evidence: [[projects/svmpx/04-source-register/sources/supporting/operations/sda-master-sample]].
