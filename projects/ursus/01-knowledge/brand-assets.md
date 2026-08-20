---
schema: hermes-kb/v2
id: kb-ursus-brand-assets
title: Ursus Trade brand asset inventory
project: ursus
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Безопасный метаданный каталог форматов и носителей бренда Ursus Trade.
aliases: [Носители Ursus Trade, Форматы бренд-файлов Ursus Trade, Инвентарь Ursus Trade]
tags: [ursus, branding, assets, inventory]
source_ids:
  - src-local-ursus-assets-6218347c
  - src-local-ursus-pptx-df09fdba
  - src-local-ursus-guidebook-89d50152
derived:
  method: filesystem-and-package-metadata
  generated_at: 2026-08-20T00:00:00Z
  extractor_version: manual-safe-audit-v1
created: 2026-08-20
updated: 2026-08-20
---

# Ursus Trade brand asset inventory

После исключения трёх временных Office lock-файлов дерево содержит 55 файлов:
19 AI, 18 PNG, 9 PDF, 5 JPEG, 2 TTF, 1 DOC и 1 PPTX. Варианты логотипа и знака
представлены в RGB/CMYK и в blue/dark-blue/black/white исполнениях.

Носители: большой подарочный пакет, пакет для бутылки, визитка, фирменный
бланк, ручка, кепка, дверная вывеска, подпись электронной почты и презентация.
Основной PPTX-шаблон содержит 18 слайдов. Брендбук — 29 страниц и перечисляет
те же носители; это подтверждает назначение файлов, но не их production-status.

Evidence:

- [[projects/ursus/04-source-register/brand-assets-directory]]
- [[projects/ursus/04-source-register/presentation-template]]
- [[projects/ursus/04-source-register/brand-guidebook]]
