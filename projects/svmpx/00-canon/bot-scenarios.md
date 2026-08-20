---
schema: hermes-kb/v2
id: kb-svmpx-bot-scenarios
title: "SVMPX bot scenarios"
project: svmpx
type: canon
domain: bot-operations
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: "Каноническое историческое описание архивного Brutto: отключённые команды, статусы, ошибки и legacy Telegram-сценарии SVMPX."
aliases:
  - Сценарии бота Брутто
  - Статусы и ошибки бота
  - Какие статусы флаги и сообщения ошибок используются
  - Telegram-боты SVMPX
source_ids:
  - src-gdrive-1yNDuuMrH7e-iUlXTudIY8mMZivugPI9w2n1tfI_lUN8
  - src-gdrive-1OhNpOFjyqWciHOKPJ83Zn_Nqk-svpg04de856oVR92s
  - src-gdrive-1TZTe8Md7BFdRswSk0JRT2kYUN1nh5r2fHq8_uTEtkkI
  - src-gdrive-175yflG6P0QmxAqTzalrCkTOs7LX8RKq8I8WuUMAgDxI
  - src-gdrive-1xWgD6_MIpSkKPwVfNb05K6O39JA76BOy
  - src-gdrive-1NbUlBCwIyXCI8U-hrT0BF6yZvEMIJ9a7
  - src-gdrive-1H8Ei74PQgrnQKcWBzJtoHoDZvRY1cBcW
  - src-gdrive-16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh
related:
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/bot-brutto-scenarios]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/flags-and-statuses]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/chatbots-messages]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/tg-chatbots]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-request]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/purchase-order-formation]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]"
created: 2026-08-19
updated: 2026-08-20
review_at: null
tags: [svmpx, bot, telegram, brutto, operations]
---

# SVMPX bot scenarios

> Каноническое описание архивного Brutto и исторических bot-сценариев. Оно не
> утверждает, что эти функции доступны в production.

## Текущий статус, подтверждённый владельцем

Brutto является основным ботом, а не оболочкой над специализированными ботами.
Сейчас его операционные функции, включая уведомления, загрузку XLSX, `/help`,
статистику и создание записей, выключены. Когда write-сценарии работали, бот
сначала показывал предварительный результат и запрашивал подтверждение; запись
не должна была изменяться без подтверждения пользователя.

Владелец решил оставить Brutto в архиве; повторное включение не планируется.
Актуальные XLSX-шаблоны хранятся на Google Drive. Историческая модель доступа
предполагала возможность работы для всех пользователей, но она не является
действующей production-политикой для архивного компонента.

## Роль бота

Подтверждённая общая граница ответственности: бот ускоряет массовые загрузки, приёмку, уведомления и поиск помощи, а основная работа с карточками и исключениями остаётся в интерфейсах Airtable. Базовая бизнес-цепочка: Client Request → Client Proposal → Purchase Order → Shipments; бот предоставляет файловые входы и переходы вокруг этой цепочки.

Связанные описания: [[projects/svmpx/04-source-register/sources/documentation/client-request]], [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]], [[projects/svmpx/04-source-register/sources/documentation/purchase-order-formation]] и [[projects/svmpx/04-source-register/sources/documentation/shipments-overview]].

## Исторический универсальный импорт

Для файловых сценариев источники согласованно описывают один цикл:

1. Бот принимает XLSX и фиксирует ожидаемое действие.
2. Валидирует структуру, обязательные поля и допустимые значения.
3. Нормализует регистр, пробелы и идентификаторы, где это разрешено сценарием.
4. Выполняет дедупликацию или возвращает строки, требующие ручного решения.
5. Возвращает итог `added / updated / skipped`, ошибки и следующий шаг.

Пользовательский контекст включает `vertical`, `role`, `pending_action`, ожидаемый тип файла, последние ссылки на шаблоны и последний объект. `/cancel` должен сбрасывать состояние, `/status` — показывать действие и ожидаемый ввод.

## Исторически описанные сценарии

| Сценарий | Вход и ключевая проверка | Успешный результат | Следующий шаг |
|---|---|---|---|
| SO | XLSX; обязательные колонки; поставщик; дедуп по EAN/P/N/Model/SKU; product matching | Строки оффера добавлены/обновлены, несопоставленные товары перечислены | Сбор CP в Airtable или PrePO |
| PrePO (legacy) | Устаревший сценарий ответа клиента на CP | Исторические данные сохранены только как evidence | Не используется в текущем каноническом процессе |
| ORD/PO | Связь с CP; компания/клиент; дата, валюта и Incoterms | Заказ создан, возвращён отчёт импорта | Inbound или Outbound |
| Inbound | Ровно один поставщик; валидная ссылка на order/line; объём не выше остатка | Входящая поставка создана | Приёмка IN → Received |
| Outbound | Поставщик не указан; клиент найден; есть основание CP/order; доступного объёма достаточно | Исходящая отгрузка создана | Подтверждение OUT → Received |
| IN Received | Поставка существует и не закрыта; факт неотрицательный и не выше допустимого | Записаны факт, брак/недостача и документы | При необходимости Discrepancy Report |
| OUT Received | Отгрузка существует и не закрыта; позиции согласованы | Записаны POD, расхождения и возвраты | При необходимости Discrepancy Report |
| DR | Есть связанная поставка и причина расхождения | Акт сохранён и связан с поставкой | Разбор исключения |

В CP источники отдельно подтверждают последовательность Draft → Sent to client → Agreement → Create PO / PO Created. Количество клиента вносится после возврата файла; `QTY Placed` фиксирует подтверждённое поставщиком количество. Изменения созданного PO инициируются через CP, а не прямым редактированием PO.

## Команды и ответы

Описанный целевой набор команд:

- `/start` — меню;
- `/templates` — актуальные шаблоны;
- `/help <запрос>` — до трёх статей базы знаний;
- `/my tasks` — незакрытые шаги онбординга;
- `/switch electronics|apparel` — смена вертикали;
- `/cancel` — сброс текущего состояния;
- `/status` — текущее действие и ожидаемый ввод.

Ошибки должны отвечать на три вопроса: что сломалось, где это произошло и что сделать дальше. Для импорта необходимо логировать пользователя, действие, имя файла, `added/updated/skipped`, структурированные ошибки, время начала/окончания и correlation ID.

## Карта Telegram-ботов

Источник `SVMPX TG Chatbots` подтверждает существование нескольких
специализированных legacy-точек входа: уведомления по Offers/Products и
парсингу, уведомления по Client Proposal, поиск товаров/офферов и статистика, а
также отдельный финансовый бот. Brutto утверждён владельцем как основной бот;
сейчас перечисленные функции выключены.

Имена и распределение функций считаются инвентаризацией legacy-состояния, а не утверждённой целевой архитектурой. Секретные значения из источника намеренно не перенесены.

## Противоречия

1. Источники описывают функции и несколько специализированных legacy-ботов,
   однако Brutto архивирован. Эти сценарии являются только историческим
   описанием и недоступны в production.
2. Для SO разрешён файл с несколькими поставщиками, а для Inbound действует hard stop «одна поставка — один поставщик». Это не ошибка, но правило должно быть явно закреплено в UX и валидаторе.
3. Источники используют разные варианты статусов и терминов. `PO`, `Order` и
   `ORD` утверждены как одна сущность, а `PrePO` — как устаревшая; для остальных
   терминов необходим единый машинный enum и отдельные UI-labels.

## Безопасность

Источник `SVMPX TG Chatbots` содержит действующие или исторические секреты в открытом тексте. До подключения ботов к Hermes необходимо:

1. Ротировать все обнаруженные токены.
2. Перенести секреты в server-side secret manager или защищённый `.env`.
3. Удалить секреты из рабочих документов и запретить их индексацию.
4. Хранить в KB только логические bot IDs, назначение и ссылку на секрет по имени, но не значение.

## Открытые вопросы

Для текущего архивного статуса открытых operational-вопросов нет. Если решение
о повторном включении когда-либо изменится, роли, allowlist, актуальные команды
и безопасность должны пройти новое утверждение; исторические настройки нельзя
восстанавливать автоматически.

## Источники

- [[projects/svmpx/04-source-register/sources/supporting/operations/bot-brutto-scenarios]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/flags-and-statuses]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/chatbots-messages]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/tg-chatbots]] — restricted inventory source; secret values are intentionally excluded.
- [[projects/svmpx/04-source-register/sources/documentation/client-request]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-formation]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-overview]]
