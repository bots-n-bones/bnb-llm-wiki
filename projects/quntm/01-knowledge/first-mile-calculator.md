---
schema: hermes-kb/v2
id: kb-quntm-first-mile-calculator
title: Quntm first-mile calculator tariffs and logic
project: quntm
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Каноническая регистрация Excel-источника тарифов и логики калькулятора первой мили Quntm/QuantumPost.
source_ids: ["src-intake-quntm-2be4f9dfae667fa0"]
created: 2026-08-23
updated: 2026-08-23
tags: ["quantumpost", "calculator", "first-mile", "tariffs", "internal"]
---

# Quntm first-mile calculator tariffs and logic

## Scope

The first-mile calculator source is an internal Excel workbook for Quntm/QuantumPost first-mile delivery to Hunchun. It contains one visible sheet (`Лист1`) with tariff tables and calculator formulas.

## Covered tariff blocks

The workbook covers:

- FTL without toll roads;
- FTL with toll roads;
- unified distance-based FTL rates in CNY/km by truck capacity;
- LTL by volume in CNY/m³;
- LTL by weight in CNY/kg;
- distance-based LTL by volume and by weight;
- delivery-time ranges by origin/distance.

## Calculator behavior captured from the source

The workbook includes example calculator areas for FTL and LTL. The extracted example includes route/city selection, cargo weight and volume, base cost, toll-road alternative, extra-kilometer adjustment, and delivery-time adjustment.

The source formulas were preserved in the intake package; 79 formulas were extracted from workbook XML during staging.

## Data-quality caveat

The workbook is accepted as the owner-approved source for Quntm first-mile tariff knowledge. Before using these values in a production calculator, manually verify apparent outlier cells in heavy-truck columns, including values resembling `215000`, `225500`, and `220500`, because they may be intentional tariffs or extra-zero entry errors.

## Confidentiality

These tariff tables and formulas are internal pricing knowledge. Do not publish them externally without separate approval.
