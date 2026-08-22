---
schema: hermes-kb/v2
id: kb-intake-shared-f92a1b5a4715201e
title: "05_AUTOMATION_USE_CASES_30.md — intake draft"
project: shared
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: "Unreviewed text extracted from a registered intake source."
source_ids: ["src-intake-shared-f92a1b5a4715201e"]
created: 2026-08-22
updated: 2026-08-22
tags: ["inbox", "derived", "needs-review"]
derived:
  method: "drive-inbox-intake"
  generated_at: "2026-08-22T07:57:11Z"
  extractor_version: "1"
---

# 05_AUTOMATION_USE_CASES_30.md — intake draft

> This is an unreviewed draft. It cannot override active canonical knowledge.

## Extracted content

# 30 кейсов автоматизации процессов с Hermes

## Как пользоваться каталогом

Каталог не является обещанием тридцати готовых интеграций. Он показывает, какие процессы можно собрать на примитивах Hermes Workspace и где потребуется MCP/API/экспорт. Для каждого кейса до запуска фиксируются владелец, baseline, допустимые данные, proof contract и точка человеческого решения.

### Уровни внедрения

- **S — 16–40 ч:** native/configured workflow на чистых данных, без тяжёлого connector.
- **M — 40–120 ч:** profile, knowledge, skills, delivery, QA и ограниченная адаптация.
- **L — 120–320 ч:** внешний connector, security mapping, сложные данные и расширенный UAT.

Трудозатраты являются плановым диапазоном на один кейс и не включают общий deployment/hardening платформы. Экономический эффект измеряется как `(ручной цикл − цикл после Hermes) × число циклов − стоимость эксплуатации`.

## Сводка

| Кластер | Кейсы | Основная ценность |
|---|---:|---|
| Knowledge и документы | 1–6 | Быстрый поиск, источники, актуальность и протоколирование. |
| Управление работой | 7–12 | Routing, статусы, решения, review и handoff. |
| Продажи и клиенты | 13–18 | Research, предложения, feedback и support drafts. |
| HR, legal, procurement, finance | 19–24 | Стандартизация подготовки без передачи решения машине. |
| Engineering и operations | 25–30 | Repro, review, release evidence, health и readiness. |

## 1. Триаж входящих документов

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Реализовано; S — 16–40 ч |
| **Владелец процесса** | Операционный офис / knowledge steward |
| **Проблема и baseline** | Документы вручную раскладываются по папкам; baseline: время обработки, доля ошибочной классификации и backlog. |
| **Триггер** | Загрузка или синхронизация нового файла. |
| **Входы** | PDF, DOCX, PPTX, XLSX/XLSM и метаданные источника. |
| **Маршрут Hermes** | inbox-triage классифицирует discard/task/research/knowledge → km-agent проверяет назначение → человек принимает candidate. |
| **Результат** | Карточка документа, класс, причина, owner и очередь review. |
| **Proof contract** | Исходный файл, extraction status, выбранный класс и объяснение доступны в артефакте. |
| **Human approval** | Публикация в durable knowledge только после review. |
| **Интеграции и данные** | Native Files/Knowledge; внешнее DMS требует MCP/API. Retention следует политике исходного документа. |
| **Fallback** | Неподдерживаемый или повреждённый файл помещается в quarantine с причиной. |
| **KPI** | Среднее время до классификации; backlog; доля исправленных человеком классов. |
| **Регулярные затраты** | 2–6 ч/мес на taxonomy и исключения. |

## 2. Загрузка корпоративной базы знаний

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Реализовано; M — 40–120 ч |
| **Владелец процесса** | Knowledge owner / руководители функций |
| **Проблема и baseline** | Регламенты и справочные материалы разрознены; baseline: время поиска и доля вопросов без ответа. |
| **Триггер** | Старт пилота, новая версия документа или плановая синхронизация. |
| **Входы** | Утверждённые документы, владельцы, версия, срок актуальности и уровень доступа. |
| **Маршрут Hermes** | Files → extraction → candidate → duplicate/conflict check → km-agent → human approve. |
| **Результат** | Индексируемая knowledge base с provenance и status каждого источника. |
| **Proof contract** | Каждая запись связана с исходником, датой, owner и решением review. |
| **Human approval** | Только knowledge steward переводит candidate в approved. |
| **Интеграции и данные** | Native; SharePoint/Drive/DMS требует connector. Retention наследуется от source-of-record. |
| **Fallback** | Материал без владельца или версии остаётся candidate/quarantine. |
| **KPI** | Доля утверждённых документов в индексе; search success; время ответа. |
| **Регулярные затраты** | 8–24 ч/мес на обновление и drift review. |

## 3. Поиск дубликатов и конфликтов знаний

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Реализовано; S — 16–40 ч |
| **Владелец процесса** | Knowledge steward |
| **Проблема и baseline** | Разные документы дают несовместимые правила; baseline: число конфликтов, найденных после ошибки. |
| **Триггер** | Поступление нового candidate или плановый аудит. |
| **Входы** | Candidate, approved knowledge и metadata/version. |
| **Маршрут Hermes** | km-agent сравнивает содержание → duplicate/conflict/quarantine → формирует evidence → owner решает. |
| **Результат** | Очередь дубликатов и конфликтов с вариантами merge/replace/reject. |
| **Proof contract** | Показаны обе версии, совпавшие фрагменты и причина классификации. |
| **Human approval** | Merge, replace и удаление утверждает владелец источника. |
| **Интеграции и данные** | Native Knowledge. Чувствительные документы остаются в локальном контуре. |
| **Fallback** | При низкой уверенности — quarantine без автоматического изменения. |
| **KPI** | Конфликты до публикации; среднее время разрешения; повторные инциденты. |
| **Регулярные затраты** | 2–8 ч/мес. |

## 4. Аудит актуальности SOP и регламентов

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Quality/compliance owner |
| **Проблема и baseline** | Процедуры устаревают незаметно; baseline: доля SOP без review date и число отклонений. |
| **Триггер** | Ежемесячный Job или новая версия внешнего требования. |
| **Входы** | Approved SOP, review dates, изменения систем и нормативные источники. |
| **Маршрут Hermes** | Job → km-agent/researcher → diff и impact list → owner review. |
| **Результат** | Реестр устаревших разделов, доказательства и проект задач обновления. |
| **Proof contract** | Каждое замечание содержит текущий текст, новое основание и источник. |
| **Human approval** | Изменение source-of-record выполняется человеком. |
| **Интеграции и данные** | Web/MCP для внешних требований; внутренние документы native. |
| **Fallback** | Если источник недоступен, отчёт помечает gap и не делает вывод. |
| **KPI** | SOP reviewed on time; средний age; число просроченных remediation. |
| **Регулярные затраты** | 4–12 ч/мес. |

## 5. Внутренние ответы с обязательными источниками

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Service desk / knowledge owner |
| **Проблема и baseline** | Сотрудники получают разные ответы и тратят время на поиск; baseline: handle time и escalation rate. |
| **Триггер** | Вопрос сотрудника в Workspace или утверждённом канале. |
| **Входы** | Вопрос, роль пользователя, approved knowledge и access scope. |
| **Маршрут Hermes** | orchestrator → km-agent retrieval → researcher при необходимости → ответ с citations. |
| **Результат** | Краткий ответ, ссылки на источники, uncertainty и следующий шаг. |
| **Proof contract** | Проверяемые утверждения имеют источник; unsupported claims явно помечены. |
| **Human approval** | Чувствительные HR/legal/finance ответы проверяет профильный владелец. |
| **Интеграции и данные** | Native Knowledge; Slack/Teams/email требует connector. |
| **Fallback** | При отсутствии источника — запрос уточнения или эскалация, без выдуманного ответа. |
| **KPI** | Source coverage; first-contact resolution; время ответа; acceptance rate. |
| **Регулярные затраты** | 4–16 ч/мес. |

## 6. Расшифровка встречи → решения и задачи

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; S — 16–40 ч |
| **Владелец процесса** | PMO / руководитель команды |
| **Проблема и baseline** | Решения теряются в расшифровках; baseline: время протокола и доля задач без owner/date. |
| **Триггер** | Появление готовой расшифровки после встречи. |
| **Входы** | TXT/DOCX transcript, участники, проект и шаблон протокола. |
| **Маршрут Hermes** | inbox-triage → orchestrator выделяет решения/риски/actions → reviewer проверяет соответствие transcript. |
| **Результат** | Протокол, decisions, action items, owners, due dates и draft tasks. |
| **Proof contract** | Каждый пункт связан с фрагментом transcript или помечен как inference. |
| **Human approval** | Создание/отправка задач и публикация протокола — после проверки организатора. |
| **Интеграции и данные** | Native для файла; Zoom/Meet/calendar/task tracker требуют connector. |
| **Fallback** | Неясные owner/date попадают в список уточнений. |
| **KPI** | Время выпуска протокола; action completeness; доля принятых без правки. |
| **Регулярные затраты** | 1–4 ч/мес на шаблоны. |

## 7. Триаж внутренних запросов

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; S — 16–40 ч |
| **Владелец процесса** | Операционный офис / shared services |
| **Проблема и baseline** | Общая очередь смешивает вопросы, задачи и знания; baseline: first response и misroute rate. |
| **Триггер** | Новый запрос или документ во входящей очереди. |
| **Входы** | Текст, вложения, автор, подразделение и SLA class. |
| **Маршрут Hermes** | inbox-triage → discard/task/research/knowledge → owner/priority → optional task. |
| **Результат** | Категория, assignee, priority, due rule и причина маршрутизации. |
| **Proof contract** | Исходный запрос и routing rationale сохранены. |
| **Human approval** | Высокий приоритет и внешняя коммуникация подтверждаются диспетчером. |
| **Интеграции и данные** | Native Tasks/Knowledge; почта/service desk требует connector. |
| **Fallback** | Low-confidence запрос направляется человеку без автоматического SLA обещания. |
| **KPI** | First response; routing accuracy; backlog age; reopen rate. |
| **Регулярные затраты** | 4–12 ч/мес. |

## 8. Еженедельный статус портфеля проектов

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | PMO / операционный директор |
| **Проблема и baseline** | Статусы собираются вручную и не сопоставимы; baseline: часы PM и доля просроченных обновлений. |
| **Триггер** | Еженедельный Job. |
| **Входы** | Tasks/Kanban, mission checkpoints, решения, риски и комментарии владельцев. |
| **Маршрут Hermes** | Job → strategist/orchestrator → нормализация RAG → reviewer проверяет unsupported status. |
| **Результат** | Executive summary, milestones, blockers, decisions и next week. |
| **Proof contract** | Каждый статус связан с задачей/checkpoint; отсутствие данных видно. |
| **Human approval** | Руководитель утверждает внешний/совет-директоров вариант. |
| **Интеграции и данные** | Native для Hermes data; Jira/Asana/ERP требуют connector. |
| **Fallback** | Проект без свежих данных получает статус data gap, не green. |
| **KPI** | Время подготовки; freshness; доля решений закрытых в срок. |
| **Регулярные затраты** | 4–12 ч/мес. |

## 9. Декомпозиция сложной инициативы

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Реализовано; M — 40–120 ч |
| **Владелец процесса** | Руководитель инициативы |
| **Проблема и baseline** | Большая цель стартует без зависимостей и критериев готовности; baseline: replanning и missed dependencies. |
| **Триггер** | Создание mission в Conductor/Swarm. |
| **Входы** | Objective, scope, ограничения, сроки, доступные workers и evidence requirements. |
| **Маршрут Hermes** | orchestrator декомпозирует → dependency graph → назначает workers → controlled batches до пяти assignments. |
| **Результат** | План задач, роли, dependencies, checkpoints и proof contracts. |
| **Proof contract** | У каждой задачи есть owner, вход, выход и критерий завершения. |
| **Human approval** | Запуск затратных/внешних веток и изменение scope подтверждает sponsor. |
| **Интеграции и данные** | Native Swarm; внешние системы — отдельные tools/connectors. |
| **Fallback** | Неразрешимая зависимость создаёт checkpoint `needs input`. |
| **KPI** | Lead time; blocked time; rework; доля задач с принятым proof. |
| **Регулярные затраты** | Зависит от числа missions; 2–8 ч governance/мес. |

## 10. Эскалация блокеров и очереди решений

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Реализовано; S — 16–40 ч |
| **Владелец процесса** | PMO / руководитель подразделения |
| **Проблема и baseline** | Блокеры остаются в чатах; baseline: blocked days и missed decision dates. |
| **Триггер** | Stalled worker, просроченный checkpoint или ручная отметка. |
| **Входы** | Run state, logs, tasks, dependency и предыдущие решения. |
| **Маршрут Hermes** | orchestrator/ops-watch собирает evidence → формулирует варианты → создаёт decision request. |
| **Результат** | Краткая причина, impact, варианты, recommendation и deadline решения. |
| **Proof contract** | Логи/checkpoints подтверждают факт блокировки. |
| **Human approval** | Решение принимает named owner; Hermes не выбирает бизнес-риск самостоятельно. |
| **Интеграции и данные** | Native; delivery в мессенджер требует настройки. |
| **Fallback** | При нехватке данных — запрос конкретного input, а не общий alert. |
| **KPI** | Mean blocked time; decision latency; повторные эскалации. |
| **Регулярные затраты** | 1–4 ч/мес. |

## 11. Управление review/approval queue

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; S — 16–40 ч |
| **Владелец процесса** | Quality owner / руководитель функции |
| **Проблема и baseline** | Результаты AI принимаются неформально; baseline: rework и отсутствие traceability. |
| **Триггер** | Завершённый артефакт, candidate или рискованное действие. |
| **Входы** | Output, proof contract, reviewer findings и risk class. |
| **Маршрут Hermes** | Reviewer → QA при необходимости → accept/rework/escalate → human greenlight. |
| **Результат** | Очередь решений с evidence, SLA и ответственным. |
| **Proof contract** | Версия артефакта, проверки и decision записаны вместе. |
| **Human approval** | Всегда человек для external/destructive/sensitive actions. |
| **Интеграции и данные** | Native checkpoints/tasks; корпоративный approval system требует connector. |
| **Fallback** | Просрочка эскалируется резервному owner без автоодобрения. |
| **KPI** | Review time; first-pass acceptance; overdue approvals. |
| **Регулярные затраты** | 2–8 ч/мес. |

## 12. Формирование пакета передачи проекта

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | PM / delivery lead |
| **Проблема и baseline** | Новый владелец восстанавливает контекст вручную; baseline: onboarding time и missing artifacts. |
| **Триггер** | Смена владельца, завершение этапа или закрытие проекта. |
| **Входы** | Tasks, files, decisions, risks, checkpoints, runbooks и contacts. |
| **Маршрут Hermes** | orchestrator собирает → km-agent проверяет source links → reviewer completeness check. |
| **Результат** | Handoff document, open items, access checklist и first-week plan. |
| **Proof contract** | Каждый раздел ссылается на актуальный source-of-record. |
| **Human approval** | Сдающий и принимающий владельцы подписывают completeness. |
| **Интеграции и данные** | Native; внешние repositories/task systems требуют connector/export. |
| **Fallback** | Missing artifact фиксируется как gap с owner/date. |
| **KPI** | Time-to-productivity; missing item rate; follow-up questions. |
| **Регулярные затраты** | На событие; шаблон 1–2 ч/квартал. |

## 13. Исследование лида или компании перед продажей

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Требует коннектора; M — 40–120 ч |
| **Владелец процесса** | Sales / business development |
| **Проблема и baseline** | Менеджер тратит время на разрозненный research; baseline: prep time и meetings without context. |
| **Триггер** | Новый квалифицированный лид или назначенная встреча. |
| **Входы** | Название компании, CRM export, сайт, публичные источники и ICP criteria. |
| **Маршрут Hermes** | researcher собирает источники → strategist формирует hypotheses → reviewer проверяет citations. |
| **Результат** | Account brief: профиль, сигналы, риски, вопросы и персонализированный angle. |
| **Proof contract** | Факты имеют URL/дату; предположения отделены от фактов. |
| **Human approval** | Менеджер утверждает использование и любые внешние сообщения. |
| **Интеграции и данные** | CRM enrichment/browser/MCP; соблюдать privacy и purpose limitation. |
| **Fallback** | При конфликте данных показываются версии и uncertainty. |
| **KPI** | Prep time; meeting-to-next-step; factual correction rate. |
| **Регулярные затраты** | 4–12 ч/мес плюс API. |

## 14. Подготовка ответа на тендер/RFP

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; L — 120–320 ч |
| **Владелец процесса** | Sales operations / bid manager |
| **Проблема и baseline** | Ответ собирается из разных владельцев и старых формулировок; baseline: total hours и missed requirements. |
| **Триггер** | Получен RFP и принято bid/no-bid решение. |
| **Входы** | RFP, compliance matrix, approved company facts, архитектура, цены и шаблон. |
| **Маршрут Hermes** | inbox-triage → orchestrator workstreams → researcher/km-agent evidence → reviewer completeness. |
| **Результат** | Draft response, compliance matrix, gaps, owners и evidence pack. |
| **Proof contract** | Каждый requirement сопоставлен с ответом, источником и статусом. |
| **Human approval** | Цена, обязательства, legal и финальная отправка — только людьми. |
| **Интеграции и данные** | Native documents; CRM/proposal platform требует connector. |
| **Fallback** | Неподтверждённое требование остаётся gap, не заполняется выдумкой. |
| **KPI** | Hours/RFP; requirement coverage; late submissions; win/loss learning. |
| **Регулярные затраты** | На тендер; 4–8 ч/квартал на knowledge refresh. |

## 15. Персонализация коммерческого предложения

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Sales / presales |
| **Проблема и baseline** | Предложения шаблонны или создаются слишком долго; baseline: turnaround и ручные правки. |
| **Триггер** | Opportunity достигла согласованной стадии. |
| **Входы** | Approved template, account brief, scope, pricing inputs и constraints. |
| **Маршрут Hermes** | strategist формирует value narrative → researcher подтверждает account facts → reviewer проверяет claims. |
| **Результат** | Персонализированный draft, assumptions и список данных для уточнения. |
| **Proof contract** | Компания, проблема и обещания связаны с подтверждёнными источниками. |
| **Human approval** | Цена, SLA, юридические обещания и отправка — человек. |
| **Интеграции и данные** | CRM/CPQ/email требуют connector; документ можно создать из export. |
| **Fallback** | При неполных данных создаётся skeleton и question list. |
| **KPI** | Turnaround; correction count; approval cycle; conversion after baseline. |
| **Регулярные затраты** | 2–8 ч/мес на шаблоны. |

## 16. Тематический анализ клиентской обратной связи

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Product / customer experience |
| **Проблема и baseline** | Отзывы читаются выборочно; baseline: time-to-insight и uncategorized share. |
| **Триггер** | Еженедельный/ежемесячный export или milestone исследования. |
| **Входы** | CSV/XLSX/DOCX export отзывов, channel, date, segment и privacy rules. |
| **Маршрут Hermes** | researcher кластеризует → strategist связывает impact → reviewer проверяет примеры и частоты. |
| **Результат** | Themes, frequency, representative examples, severity и backlog candidates. |
| **Proof contract** | Каждая тема имеет count, выборку примеров и методику. |
| **Human approval** | Product owner принимает приоритет; PII минимизируется. |
| **Интеграции и данные** | Export native; live CRM/support platform требует connector. |
| **Fallback** | Слишком малая выборка помечается как non-representative. |
| **KPI** | Time-to-insight; coverage; accepted backlog items; повторяемость тем. |
| **Регулярные затраты** | 4–16 ч/мес. |

## 17. Черновик ответа службы поддержки

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Требует коннектора; M — 40–120 ч |
| **Владелец процесса** | Customer support |
| **Проблема и baseline** | Повторные вопросы требуют ручного поиска; baseline: handle time, escalation и QA score. |
| **Триггер** | Новый ticket согласованного класса. |
| **Входы** | Ticket, approved KB, customer context и response policy. |
| **Маршрут Hermes** | inbox-triage → km-agent retrieval → draft → reviewer checks policy/source. |
| **Результат** | Черновик ответа, citations, uncertainty и suggested disposition. |
| **Proof contract** | Рекомендации основаны на KB и policy; unsupported action не предлагается. |
| **Human approval** | Агент поддержки отправляет ответ; auto-send вне пилота. |
| **Интеграции и данные** | Service desk/CRM/email через MCP/API; PII retention по политике. |
| **Fallback** | Нет источника или высокий risk → human escalation. |
| **KPI** | Handle time; first-contact resolution; QA score; correction rate. |
| **Регулярные затраты** | 8–24 ч/мес на KB и QA. |

## 18. Репакетирование контента и очередь публикаций

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Marketing / communications |
| **Проблема и baseline** | Один материал редко используется повторно; baseline: production time и consistency defects. |
| **Триггер** | Утверждённый long-form материал или событие. |
| **Входы** | Approved source, tone guide, channel limits и campaign brief. |
| **Маршрут Hermes** | strategist задаёт angles → researcher проверяет facts → variants → reviewer brand/compliance. |
| **Результат** | Drafts для post, newsletter, FAQ и short summary с approval queue. |
| **Proof contract** | Все варианты связаны с approved source; новые claims выделены. |
| **Human approval** | Публикация и отправка только после marketing/legal review. |
| **Интеграции и данные** | CMS/social/email требуют connector. |
| **Fallback** | Несоответствие tone/fact возвращается на rework, не публикуется. |
| **KPI** | Asset turnaround; reuse factor; approval iterations; engagement measured separately. |
| **Регулярные затраты** | 4–12 ч/мес. |

## 19. Пакет адаптации нового сотрудника

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | HR / hiring manager |
| **Проблема и baseline** | Онбординг зависит от конкретного коллеги; baseline: manager hours и time-to-productivity. |
| **Триггер** | Подтверждённый выход сотрудника. |
| **Входы** | Role, approved policies, SOP, team contacts и first-month goals. |
| **Маршрут Hermes** | km-agent собирает approved sources → strategist адаптирует plan → reviewer проверяет completeness. |
| **Результат** | Role-specific checklist, FAQ, first-week plan и learning path. |
| **Proof contract** | Политики и обязанности ссылаются на действующие источники. |
| **Human approval** | HR и hiring manager утверждают пакет; доступы выдаются отдельно. |
| **Интеграции и данные** | HRIS/calendar/access management требуют connector. |
| **Fallback** | Отсутствующий policy фиксируется как gap, не заменяется общим советом. |
| **KPI** | Time-to-productivity; manager hours; onboarding completion; new-hire rating. |
| **Регулярные затраты** | 2–8 ч/мес на роли/политики. |

## 20. Подготовка вакансии и интервью-пакета

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; S — 16–40 ч |
| **Владелец процесса** | HR / hiring manager |
| **Проблема и baseline** | Критерии вакансии и вопросы интервью непоследовательны; baseline: prep time и scorecard completeness. |
| **Триггер** | Открытие утверждённой позиции. |
| **Входы** | Role profile, компетенции, salary policy и compliance rules. |
| **Маршрут Hermes** | strategist формирует draft → km-agent сверяет policies → reviewer ищет bias/unsupported criteria. |
| **Результат** | Vacancy draft, structured interview guide и scorecard. |
| **Proof contract** | Каждый критерий связан с ролью; дискриминационные признаки исключены. |
| **Human approval** | HR утверждает; Hermes не ранжирует и не отклоняет кандидатов автоматически. |
| **Интеграции и данные** | ATS publishing требует connector и отдельный review. |
| **Fallback** | Неясные требования возвращаются hiring manager как questions. |
| **KPI** | Prep time; scorecard usage; interviewer consistency; compliance corrections. |
| **Регулярные затраты** | На вакансию. |

## 21. Мониторинг изменений политик и требований

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Требует коннектора; L — 120–320 ч |
| **Владелец процесса** | Compliance / legal operations |
| **Проблема и baseline** | Изменения внешних требований обнаруживаются поздно; baseline: detection lag и overdue actions. |
| **Триггер** | Scheduled research Job или alert из доверенного источника. |
| **Входы** | Whitelist источников, темы, юрисдикции, действующие policies. |
| **Маршрут Hermes** | researcher отслеживает → km-agent diff → strategist impact map → legal review. |
| **Результат** | Change brief, affected documents/processes, uncertainty и action list. |
| **Proof contract** | Дата, первоисточник и изменившийся фрагмент обязательны. |
| **Human approval** | Юридическую интерпретацию и изменение policy делает профильный специалист. |
| **Интеграции и данные** | Web/MCP/subscription sources; retention по compliance policy. |
| **Fallback** | Недоступный или непервичный источник помечается, вывод не утверждается. |
| **KPI** | Detection lag; source coverage; overdue remediation; false positives. |
| **Регулярные затраты** | 8–24 ч/мес плюс подписки. |

## 22. Сравнение договоров и список вопросов для юриста

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Legal operations / procurement |
| **Проблема и baseline** | Первичное сравнение версий занимает время; baseline: review hours и missed changes. |
| **Триггер** | Новая версия договора или предложение контрагента. |
| **Входы** | Две версии, clause playbook и утверждённые positions. |
| **Маршрут Hermes** | researcher/diff → strategist группирует deviations → reviewer проверяет traceability. |
| **Результат** | Clause matrix, изменения, risk questions и список отсутствующих данных. |
| **Proof contract** | Каждый пункт содержит номера разделов и точные ссылки на версии. |
| **Human approval** | Юридическая оценка, переговорная позиция и подписание — только юрист/уполномоченный. |
| **Интеграции и данные** | DMS/e-signature требует connector; документы в ограниченном retention scope. |
| **Fallback** | Скан без доступного текста направляется на OCR/manual review. |
| **KPI** | First-pass review time; detected changes; legal correction rate. |
| **Регулярные затраты** | На договор; playbook refresh ежеквартально. |

## 23. Сравнение поставщиков и evidence matrix

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Procurement / business owner |
| **Проблема и baseline** | Предложения несопоставимы и решения теряют основания; baseline: analysis hours и missing criteria. |
| **Триггер** | Получены предложения минимум двух поставщиков. |
| **Входы** | RFP criteria, proposals, цены, SLA, references и risk constraints. |
| **Маршрут Hermes** | researcher извлекает facts → strategist нормализует criteria → reviewer проверяет evidence. |
| **Результат** | Comparison matrix, gaps, TCO assumptions, risks и recommendation options. |
| **Proof contract** | Каждая оценка имеет источник/страницу; субъективный weight указан. |
| **Human approval** | Выбор поставщика и коммерческое решение принимает комитет. |
| **Интеграции и данные** | Procurement/ERP требует connector; можно начать с файлов. |
| **Fallback** | Несравнимое поле отмечается unknown, не нормализуется искусственно. |
| **KPI** | Analysis time; missing criteria; decision cycle; post-selection variance. |
| **Регулярные затраты** | На закупку. |

## 24. Предварительная проверка счетов и расходов

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Требует коннектора; L — 120–320 ч |
| **Владелец процесса** | Finance operations |
| **Проблема и baseline** | Ошибки реквизитов и политик ищутся поздно; baseline: manual touches и exception rate. |
| **Триггер** | Получен счёт/expense export до проведения операции. |
| **Входы** | Readable invoice/export, PO, vendor master и expense policy. |
| **Маршрут Hermes** | inbox-triage → extraction → rules/profile checks → exception report → finance review. |
| **Результат** | Checklist: совпадение PO/vendor/sum/tax fields, дубликат, missing data и risk flags. |
| **Proof contract** | Каждый flag связан с полем документа и правилом. |
| **Human approval** | Hermes не создаёт платёж и не проводит запись; решение принимает finance. |
| **Интеграции и данные** | ERP/accounting/OCR/bank требуют connector; financial retention и least privilege обязательны. |
| **Fallback** | Неуверенное распознавание или mismatch → manual queue. |
| **KPI** | Touch time; pre-posting error detection; duplicate flags; false positives. |
| **Регулярные затраты** | 8–24 ч/мес плюс connector support. |

## 25. Триаж программных ошибок и repro packet

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Engineering / product support |
| **Проблема и baseline** | Issue поступают без воспроизводимости; baseline: time-to-repro и reopen rate. |
| **Триггер** | Новый issue, incident report или log bundle. |
| **Входы** | Описание, версия, environment, logs, screenshots и expected behavior. |
| **Маршрут Hermes** | inbox-triage → qa воспроизводит → reviewer severity/security check → task. |
| **Результат** | Repro steps, actual/expected, evidence, severity, suspected area и owner. |
| **Proof contract** | Команды, screenshots/log excerpts и environment зафиксированы. |
| **Human approval** | Severity и приоритет подтверждает product/engineering owner. |
| **Интеграции и данные** | GitHub/Jira/Sentry требуют connector. |
| **Fallback** | Невоспроизводимое issue получает exact missing evidence list. |
| **KPI** | Time-to-repro; complete issue rate; reopen; duplicate rate. |
| **Регулярные затраты** | 4–12 ч/мес. |

## 26. Исправление через Builder → Reviewer → QA

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; L — 120–320 ч |
| **Владелец процесса** | Engineering lead |
| **Проблема и baseline** | Изменения проходят без независимой проверки; baseline: escaped defects и review cycle. |
| **Триггер** | Утверждённая scoped engineering task. |
| **Входы** | Issue/repro, repository, constraints, acceptance tests и branch policy. |
| **Маршрут Hermes** | orchestrator → builder patch/tests → reviewer regression/security → qa smoke → report. |
| **Результат** | Scoped change, tests, findings, evidence и merge readiness. |
| **Proof contract** | Diff, test commands/results и QA evidence доступны. |
| **Human approval** | Merge, release и deploy выполняются только после human greenlight. |
| **Интеграции и данные** | Git hosting/CI/browser tools; credentials least privilege. |
| **Fallback** | Failed test/review возвращает rework; нет force merge. |
| **KPI** | Lead time; first-pass review; escaped defects; rollback rate. |
| **Регулярные затраты** | На change; governance 4–8 ч/мес. |

## 27. Регрессионный smoke и release-readiness

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | QA / release manager |
| **Проблема и baseline** | Релизное решение не имеет единого evidence pack; baseline: manual checklist и incidents after release. |
| **Триггер** | Release candidate или production hotfix. |
| **Входы** | Commit/image, change list, test plan, health endpoints и known risks. |
| **Маршрут Hermes** | qa browser/CLI smoke → reviewer findings → ops-watch health → go/no-go summary. |
| **Результат** | Pass/fail matrix, evidence, residual risks и draft release notes. |
| **Proof contract** | Каждый critical path имеет команду/скриншот/результат. |
| **Human approval** | Release manager принимает go/no-go и запускает deploy. |
| **Интеграции и данные** | CI/CD и environments требуют доступа; destructive actions gated. |
| **Fallback** | Любой P0 failure даёт no-go, а не условный success. |
| **KPI** | Smoke duration; escaped critical defects; rollback; evidence completeness. |
| **Регулярные затраты** | На релиз. |

## 28. Мониторинг upstream и зависимостей

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Maintainer / security owner |
| **Проблема и baseline** | Обновления, CVE и deprecation обнаруживаются несистемно; baseline: detection lag и overdue patches. |
| **Триггер** | Еженедельный Job или advisory/release event. |
| **Входы** | Dependency manifests, upstream releases, advisories и local custom diff. |
| **Маршрут Hermes** | maintainer/researcher → impact analysis → reviewer reachability → task proposals. |
| **Результат** | Update brief, affected components, severity, test scope и recommended window. |
| **Proof contract** | Advisory/release links, installed version и dependency path. |
| **Human approval** | Upgrade, code change и deploy отдельно согласуются. |
| **Интеграции и данные** | GitHub/registries/security feeds через web/API. |
| **Fallback** | Неясная reachability остаётся investigation, не false all-clear. |
| **KPI** | Detection lag; patch SLA; false positives; failed updates. |
| **Регулярные затраты** | 4–12 ч/мес. |

## 29. Health digest и первичная диагностика инцидента

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Настраивается; M — 40–120 ч |
| **Владелец процесса** | Ops/SRE |
| **Проблема и baseline** | Сигналы сервисов разрознены; baseline: detection/diagnosis time. |
| **Триггер** | Scheduled health Job, alert или ручной запрос. |
| **Входы** | Gateway/Dashboard/Workspace health, container status, Jobs и logs. |
| **Маршрут Hermes** | ops-watch собирает → correlates symptoms → hypothesis → safe remediation plan → owner. |
| **Результат** | Health digest или incident packet с impact, evidence и next steps. |
| **Proof contract** | Timestamped probes/logs и distinction fact/hypothesis. |
| **Human approval** | Restart, config, credential и deploy changes требуют operator greenlight. |
| **Интеграции и данные** | Native health; external monitoring/on-call требует connector. |
| **Fallback** | Недоступный probe фиксируется как unknown; не интерпретируется healthy. |
| **KPI** | MTTD; time-to-diagnostic-packet; repeated incidents; alert quality. |
| **Регулярные затраты** | 8–24 ч/мес. |

## 30. Сводка сбоев Jobs, MCP и provider readiness

| Поле | Описание |
|---|---|
| **Статус / трудоёмкость** | Реализовано/настраивается; S — 16–40 ч |
| **Владелец процесса** | Automation owner / Ops |
| **Проблема и baseline** | Автоматизации молча деградируют из-за расписания, provider или connector; baseline: missed runs и manual checks. |
| **Триггер** | Ежедневный Job и capability change. |
| **Входы** | Job history, MCP list/test/logs, connection status и provider metadata без секретов. |
| **Маршрут Hermes** | ops-watch → failed/missed grouping → owner/action mapping → delivery. |
| **Результат** | Digest: failed/missed Jobs, connector/provider issue, impact и next action. |
| **Proof contract** | Run IDs, timestamps, capability probes и error category. |
| **Human approval** | Изменение credentials/config и retry с внешним эффектом подтверждает owner. |
| **Интеграции и данные** | Native full mode; config-only fallback имеет ограниченную диагностику. |
| **Fallback** | Unknown capability явно показывается; секреты не читаются и не выводятся. |
| **KPI** | Missed run rate; mean time to owner; repeat failures; stale connector count. |
| **Регулярные затраты** | 2–8 ч/мес. |

## Рекомендуемый первый пакет

Для среднего бизнеса без заранее выбранной отраслевой интеграции оптимальны кейсы 2+5, 6 и 8+10: knowledge base с ответами по источникам, meeting-to-actions и weekly project status с blocker escalation. Они используют основное ядро Hermes, быстро дают измеримый baseline и не требуют выдавать системе право на платёж, публикацию или юридическое решение.

## Общие правила безопасности

1. External write отделяется от анализа и draft.
2. Платёж, публикация, найм/отказ, юридическое решение, credential change, merge и deploy требуют человека.
3. Нет источника — нет уверенного фактического утверждения.
4. Connector имеет минимальный scope, named owner, retention и tested fallback.
5. Логи и артефакты не содержат secrets или избыточные персональные данные.
