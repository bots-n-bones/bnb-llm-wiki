---
schema: hermes-kb/v2
id: kb-intake-hermes-b7006d9a6c9951cd
title: "Сводка реализованных контуров Hermes — intake draft"
project: hermes
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: "Unreviewed text extracted from a registered intake source."
source_ids: ["src-intake-hermes-b7006d9a6c9951cd"]
created: 2026-08-24
updated: 2026-08-24
tags: ["inbox", "derived", "needs-review"]
derived:
  method: "hermes-message-intake"
  generated_at: "2026-08-24T07:06:18Z"
  extractor_version: "1"
---

# Сводка реализованных контуров Hermes — intake draft

> This is an unreviewed draft. It cannot override active canonical knowledge.

## Extracted content

# Сводка реализованных контуров Hermes

> Статус: intake-кандидат для проекта `hermes`. Сводка фиксирует состояние на момент подготовки; это не самостоятельная каноническая спецификация.

- **Telegram-интерфейс Hermes** — сообщения, запросы к базе знаний, загрузка файлов и ответы в проектных группах.
- **Shared Task Manager** — общий API-трекер задач, исполнителей, сроков и статусов.
- **Native Tasks / Kanban Conductor `bnb-conductor`** — отдельная нативная доска Hermes для задач и мультиагентной работы.
- **Conductor / Swarm-пайплайн** — тестировалась цепочка ролей `researcher → architect → builder → QA → integrator`; созданы тестовые задачи и HTML-артефакты.
- **Статус Conductor** — механизм доски и запуска воркеров есть, но надёжность не доведена: наблюдались блокировки из-за дрейфа конфигураций профилей/моделей и таймаутов. Не считать полностью готовым пайплайном.
- **HTML smoke-приложения Conductor** — созданы два простых `Hello Conductor`; это тесты цепочки артефактов, не готовый пользовательский продукт.
- **Files / пользовательские файлы** — результаты задач хранятся в `Files → Tasks/<task-id>/`; системные каталоги не используются для пользовательских артефактов.
- **Google Drive integration** — OAuth-подключение Drive работает; доступны чтение метаданных, поиск файлов, ссылки и работа в каноническом корне Bots-n-Bones.
- **Канонический Drive-контур Bots-n-Bones** — закреплён единый актуальный корень проекта; прежний корень исключён из текущего использования.
- **Drive → Wiki → SQLite index** — основной контур: `Google Drive / Telegram → Intake → private staging → review → draft → owner approval → canonical release → локальный SQLite-индекс`.
- **Inbox-пайплайн** — новые файлы и сообщения сначала попадают в `00 - inbox` / intake и не становятся знаниями автоматически.
- **Review и canonical promotion** — review и канонизация разделены; канонизация требует явного решения владельца и проходит validation/release worker.
- **Provenance-пайплайн** — для знаний сохраняются Wiki-путь, ссылка на оригинал Drive, источник, статус, tier и конфиденциальность.
- **Поиск по базе знаний** — Hermes запрашивает локальный опубликованный SQLite-индекс, а не полагается на память или произвольный полнотекстовый поиск Drive.
- **Поиск документации проекта** — рабочий порядок: проверить каноническую папку Drive → запросить `active-canonical` Wiki → вернуть ссылки на Wiki/оригиналы → отдельно отметить Inbox и пустые папки.
- **Документация Hermes в KB** — индексируются модель доступа Hermes, архитектурная схема KB Hermes, PRD Hermes Workspace и governance-страницы Drive-to-Wiki.
- **Pipeline сохранения знаний из сообщений** — запросы «запиши / сохрани / добавь» проходят через intake; новые утверждения не становятся каноническими автоматически.
- **Проект «Илья»** — зарегистрирован как internal intake-запрос на отдельный проект персональной информации; без самовольной канонизации.
- **Telegram chat-export pipeline** — HTML-экспорт нормализуется в проверяемый JSONL с манифестом, хешем, количеством сообщений и возможностью дальнейшего анализа.
- **Cron-пайплайн** — подключён планировщик Hermes. `bnb-post-canonical-drive-move` работает каждые 15 минут, но последний запуск завершился ошибкой; `russian-joke-every-30-minutes` поставлен на паузу.
- **Постканонический перенос исходников Drive** — отдельный cron переносит разрешённые source-файлы из Inbox в папку проекта, сохраняя стабильный Drive ID/URL в provenance.
- **Делегирование субагентов** — доступен режим параллельных исследований/анализа с возвратом результатов в основной чат.

## Готовность

- **Работает:** Telegram, Drive-доступ, KB intake/review/release/index, поиск KB, экспорт чатов, shared task manager, файлы задач, делегирование.
- **Есть, но требует доводки:** Conductor/Swarm, native Tasks-интеграция, post-canonical Drive mover cron.
- **Тестовые артефакты, не продукты:** два HTML-приложения `Hello Conductor`.

