---
schema: hermes-kb/v2
id: kb-quntm-savimpex-case
title: Savimpex LogisticsOS case
project: quntm
type: reference
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Черновой разбор заявленного перехода Savimpex от разрозненных файлов к сквозному LogisticsOS-процессу.
aliases:
  - Кейс Savimpex
  - Пайплайн Savimpex
  - Внедрение LogisticsOS
  - Какая последовательность offers validation proposals orders shipments описана в кейсе
tags: [quntm, savimpex, logistics-os, case-study]
source_ids: [src-local-quntm-savimpex-1396366a]
created: 2026-08-20
updated: 2026-08-20
---

# Savimpex LogisticsOS case

> Неподтверждённый маркетинговый кейс; метрики требуют отдельного evidence.

Источник описывает исходное состояние как Excel, мессенджеры и локальные
папки без общего процесса. Целевая цепочка:
`offers → validation → proposals → orders → shipments`.

**Bones** в кейсе — сущности и стандарты: Products, Source Offer Lines, единый
каталог, правила quantities и статусов. **Bots** — расчёты, проверки, создание
КП и алерты. Заявленная схема внедрения занимает 13 недель: discovery (1–2),
core (3–5), commerce (6–8), logistics (9–11), go-live (12–13).

Источник заявляет: подготовка КП 4–5 часов → 40–50 минут, ×3 предложений,
−65% ошибок DDP, обработка прайса около 14 минут вместо 3–5 часов, каталог
12 000+ SKU. Эти числа не подтверждены независимыми данными и не являются
активным каноном.

Evidence: [[projects/quntm/04-source-register/savimpex-case]].
