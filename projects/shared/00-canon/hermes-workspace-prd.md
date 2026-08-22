---
schema: hermes-kb/v2
id: hermes-workspace-prd
title: Hermes Workspace PRD
project: shared
type: canon
status: active
canonical: true
owner: ilya
created: 2026-08-22
updated: 2026-08-22
confidentiality: internal
summary: Product requirements for Hermes Workspace, including chat, files, terminal, knowledge, jobs, swarm orchestration, and integrations.
aliases: [PRD Hermes Workspace, Hermes Workspace requirements]
tags: [hermes, workspace, prd, product-requirements]
source_ids: [src-intake-shared-15e134f1aa5e8f42]
source:
  kind: google-drive
  drive_file_id: 1Ts3cySKl3KMmSrHEToRwY6xrJ-47VB_6
  url: https://docs.google.com/document/d/1Ts3cySKl3KMmSrHEToRwY6xrJ-47VB_6/edit?usp=drivesdk&ouid=103073671129499618095&rtpof=true&sd=true
  mime_type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
  parent_folder_id: 10Xg3r5UUCygMiSWpog3z4Vima-b2a85N
  original_path: 00 - inbox/PRD.docx
  original_title: PRD.docx
  modified_time: 2026-08-22T07:02:53.000Z
  checksum: 353c5b220d4f3b7e0ceb76ba627aa30c37111df7b70cf46303782f8699684a1a
  revision_id: "3"
provenance:
  method: reviewed-owner-approved-conversion-from-drive-docx
  captured_at: 2026-08-22T07:14:35Z
  source_ids: [src-intake-shared-15e134f1aa5e8f42]
---

# PRD: Hermes Workspace
## Назначение продукта
Hermes Workspace — рабочий центр для управления Hermes Agent, корпоративными знаниями, задачами, файлами, терминалом и командой специализированных AI-агентов. Он превращает разовые AI-запросы в наблюдаемые и повторяемые процессы с общей памятью, доказательствами и человеческим контролем.
## Проблема
Сотрудники используют AI фрагментарно: контекст копируется вручную, ответы не привязаны к утверждённым источникам, регулярные задачи не имеют владельца и истории, а автоматическое действие либо отсутствует, либо создаёт неприемлемый риск. Руководителю нужен единый контур, в котором видны задача, исполнитель, источник, результат, проверка и точка решения человека.
## Цели
Объединить работу с AI, файлами, задачами, терминалом и знаниями в одном интерфейсе.
Делать повторяемые процессы через Profiles, Skills и Jobs.
Координировать специализированных агентов через Conductor и Swarm.
Сохранять проверяемый контекст в Memory/Knowledge.
## Функциональные требования
### FR-1. Подключение и capabilities
Система должна показывать connected, partial/enhanced или disconnected state.
UI не должен показывать функцию доступной, если соответствующая capability не подтверждена.
Provider tokens не должны передаваться в browser bundle.
### FR-2. Chat и контекст
Пользователь должен создавать и продолжать сессии, выбирать модель и прикладывать файлы.
Ответ должен передаваться потоково и показывать tool output без раскрытия секретов.
Активный запуск должен быть управляемым и иметь понятный статус.
### FR-3. Files и Terminal
Пользователь должен просматривать, читать, создавать, загружать, переименовывать и скачивать файлы в разрешённом root.
Удаление должно использовать recoverable trash там, где это поддержано.
Терминал должен работать через отдельные PTY-сессии и сохраняться между переходами интерфейса.
### FR-4. Knowledge
Система должна извлекать текст из поддерживаемых PDF, DOCX, PPTX и XLSX/XLSM.
Новый материал должен проходить candidate/review lifecycle.
Duplicate, conflict и quarantine должны быть видимы владельцу знаний.
Утверждение durable knowledge должно требовать человека.
### FR-5. Jobs и повторяемость
Владелец автоматизации должен задать profile, prompt, schedule, skills и delivery.
Job должен поддерживать pause, resume, run-now и историю результата.
Ошибка должна создавать диагностируемый результат, а не молчаливое исчезновение.
### FR-6. Swarm
Миссия должна декомпозироваться на ограниченные задания с владельцем и proof contract.
Оркестрация должна учитывать зависимости и контролируемый параллелизм.
Reviewer и QA должны быть независимыми ролями.
Merge, deploy, публикация, отправка сообщения, удаление и смена credentials должны требовать greenlight.
### FR-7. Интеграции
MCP/API-коннектор должен иметь явный scope, секреты, owner и fallback.
External write должен быть отделён от анализа и черновика.
Delivery в Telegram/Discord допустим только после серверной настройки allowlist и токенов.
## Примеры
## База знаний
База знаний позволяет помнить и выдавать конкретную информацию по проектам:
А так же заносить файлы через 00 - inbox Google Drive или Телеграм и видеть статус внесения в базу знаний:
## Автоматизация бизнес процессов
Автоматические напоминания по CRON. Отдельный таск менеджер. Запись звонков и автоматическое саммари по таскам. Вывод трендов по выбранной теме от пользователя. Работа с почтой. Лог об ошибках. Сводка недели по сотрудникам и по тому, что случилось за неделю.
