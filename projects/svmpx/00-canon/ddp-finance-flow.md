---
schema: hermes-kb/v2
id: kb-svmpx-ddp-finance-flow
title: "SVMPX DDP and finance flow"
project: svmpx
type: canon
domain: finance
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: "Черновое описание расчёта DDP, параметров формулы и финансового потока заказа от Source Offer до Client Proposal."
aliases:
  - Расчёт DDP
  - Формула DDP
  - Финансовый поток заказа
source_ids:
  - src-gdrive-1McYwf_KlJ9Q-rID0V1GU_Pj3mSvK3wS8nptYYQg5VV4
  - src-gdrive-12noCwtxbY-_A3AaBKL6t9A4eiX4akFUb
  - src-gdrive-1kQpu9whZthTykb9oltDnWgVjmnK17FkH
  - src-gdrive-1xvU7-JryYIKWNg8RSsycw5EJbB9nGGW4
  - src-gdrive-1bmHoD2jBsr15TUt7Ba7MFl5DnBk_QiPg
  - src-gdrive-11k4c1lrD1xmIIDAXqR0Vr9lqXdIBMCwR
  - src-gdrive-1NbUlBCwIyXCI8U-hrT0BF6yZvEMIJ9a7
  - src-gdrive-11SnMFpVevWV8OwlXYQau-meyUpay9KQP
related:
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/ddp-logic]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/source-offers-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/source-offers-card]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/source-offers-status-errors]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-proposal-overview]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-proposal-card]]"
  - "[[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]]"
  - "[[projects/svmpx/04-source-register/sources/supporting/operations/sda-master-sample]]"
created: 2026-08-19
updated: 2026-08-20
review_at: null
tags: [svmpx, ddp, finance, source-offers, client-proposal]
---

# SVMPX DDP and finance flow

> Каноническое описание подтверждённых правил и ограничений DDP. Страница
> намеренно не является числовым калькулятором: точная исполнимая формула
> FCL/LCL не подтверждена.

## Решения владельца

Ставки Serbian markup `7%`, Russian VAT `20%` и client margin `20%` являются
фиксированными. Если `Pcs per Pallet` отсутствует в строке оффера, используется
значение из Category связанного Product. `LC-001` хранится в Airtable, но
является устаревшей сущностью: в актуальной версии фабрики она не нужна и ничем
не заменена. Валютный курс вводится вручную. Процентные слои начисляются
последовательно на растущую расчётную базу.

Russian markup является переменным. Tariff берётся из Category связанного
Product. Если ручной валютный курс отсутствует, расчёт блокируется ошибкой.
Цена и ручной валютный курс фиксируются при создании Client Proposal.
Russian markup может задаваться как в Source Offer, так и в Client Proposal.
Если он задан в Client Proposal, это значение автоматически перекрывает
значение Source Offer. Russian markup может менять любой пользователь. Для
смешанной загрузки FCL/LCL расчёт выполняется автоматически формулами Airtable.
Назначение поля, обозначенного в источниках как `DDPL` (владелец также упомянул
`TDPL`), не подтверждено.

Tariff по умолчанию берётся из Category, но пользователь может его
переопределить. Ошибка DDP блокирует создание клиентского файла. Утверждённого
контрольного числового примера расчёта нет; до его появления Hermes не должен
представлять вычисленный числовой результат как проверенный канон.
`Product Not Found` также блокирует создание клиентского файла. Incoterms
фиксируется при создании Client Proposal вместе с ценой и валютным курсом.
Текущего исторического описания LC-001 достаточно; точную старую формулу
отдельно архивировать не требуется.
Владелец решил оставить Wiki без числового DDP-калькулятора и без эталонного
числового примера. Страница объясняет подтверждённые правила и ограничения, но
не вычисляет итоговую цену.

## Место расчёта в процессе

Source Offers — операционный слой строк предложений поставщиков: файл оффера →
документ SO → строки SOL. В строке фиксируются EXW, количество, условия оффера
и входные параметры логистики. Исторически цену DDP рассчитывала модель LC-001;
в актуальной фабрике эта сущность не используется и не имеет замены. Выбранные
SOL копируются в Client Proposal, где Finance-параметры применяются к строкам и
итоговая клиентская цена включает маржу.

Поток данных:

1. Supplier offer задаёт EXW, валюту, `Qty Offered`, `Pcs per Pallet`, срок действия и другие условия.
2. Product даёт Category и каталожные параметры, включая `Pcs per Pallet`, если они доступны.
3. Source Offer использует введённый вручную exchange rate, FCL/LCL-логистику,
   тарифы, VAT и markups.
4. В исторической версии LC-001 формировал `Final Price RU`; актуальная версия
   фабрики не использует эту сущность и не имеет заменяющей сущности.
5. Выбранная строка попадает в CP; CP Finance применяет общие изменения маржи/надбавок/курса.
6. Клиентский файл создаётся из текущих выбранных строк. После любого изменения цен или Finance-параметров файл необходимо пересоздать.

Описание Source Offers: [[projects/svmpx/04-source-register/sources/documentation/source-offers-overview]], [[projects/svmpx/04-source-register/sources/documentation/source-offers-card]] и [[projects/svmpx/04-source-register/sources/documentation/source-offers-status-errors]]. Переход в CP: [[projects/svmpx/04-source-register/sources/documentation/client-proposal-overview]], [[projects/svmpx/04-source-register/sources/documentation/client-proposal-card]] и [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]].

## Подтверждённые входы

| Вход | Источник/назначение |
|---|---|
| EXW | Цена поставщика в валюте оффера |
| Category | Выбор тарифных и других категорийных параметров |
| Qty Offered | Количество, на которое распределяется логистика |
| Pcs per Pallet | Пересчёт паллетной логистики на единицу товара; при пустом значении используется значение из Category продукта |
| Exchange rate | Перевод валютной стоимости; курс вводится вручную |
| FCL/LCL parameters | Полная или сборная загрузка, число паллет/контейнеров и шаг изменения стоимости |
| Tariff | Тариф из Category связанного Product с возможностью пользовательского override |
| VAT | Налоговый компонент расчёта |
| Markups | Сербская/российская и клиентская надбавки; часть параметров может переопределяться |

## Подтверждённая логика верхнего уровня

Источник DDP Logic задаёт последовательность компонентов:

```text
EXW
+ logistics per unit
→ Serbian markup
→ Russian tariff
→ Russian VAT
→ Russian markup
→ client margin
→ final client/DDP price
```

Это подтверждённый порядок расчётных слоёв: каждый следующий процент
начисляется на уже увеличенную базу. Фиксированные ставки Serbian markup `7%`,
Russian VAT `20%` и client margin `20%` применяются на своих этапах этой
последовательности. Tariff берётся из Category продукта. Для переменного
Russian markup ещё требуется определить источник значения и права изменения.
Историческая книга `SDA master` подтверждает набор промежуточных полей
(`DAP`, tariff, VAT, DDP и финальная цена), но не переводит исторический
пример в актуальное исполнимое правило.

## Устаревший кандидат формулы Logistics Pallet

Источник приводит следующий текстовый вариант:

```text
Logistics Pallet =
  FCL_pallet_price × FCL_containers × Pal_per_FCL
  + (One_pallet_price − (LCL_pallets − 1) × Step)
    / Pcs_per_Pallet × Goods_without_FCL
  ÷ Offered_QTY
```

Подтверждённые определения:

- `FCL_pallet_price` — стоимость паллеты при полной загрузке;
- `One_pallet_price` — базовая стоимость паллеты LCL;
- `Step` — снижение стоимости паллеты при изменении LCL-загрузки;
- `Offered_QTY` — количество единиц в оффере.

Формула перенесена как исторический кандидат, а не как исполнимое правило: в
оригинале несбалансированы скобки, не определены `Pal_per_FCL`,
`Goods_without_FCL` и точный порядок деления. `LC-001` в Airtable является
устаревшей сущностью и в актуальной фабрике не используется. Историческая
формула сохранена только как evidence; исполнимого правила из неё не создаётся.

## Статусы и контроль ошибок

- `DDP Error` означает проблему расчёта, а не коммерческий статус оффера.
- При ошибке необходимо проверить exchange rate, логистику, тариф, markup и обязательные входы.
- `Product Not Found` блокирует создание клиентского файла, потому что Category
  и каталожные параметры недоступны.
- `Markups Change` и `Tariffs Change` показывают, что вместо стандартных параметров используются изменения пользователя.
- В CP некорректные данные Source Offer или Finance могут блокировать переход по этапам без отдельного красного статуса CP.

## Противоречия

1. Источник говорит о диапазоне DDP из-за логистики и курса, а карточка SO показывает один `LC-001 Final Price RU`. Не определено, хранится ли диапазон отдельно или это только текст для клиента.
2. В CP встречается название `DDPL` / `TDPL`, но его значение владелец не смог
   подтвердить; поле нельзя использовать в ответах как определённый показатель.
3. Историческая формула логистики не фиксирует единицы измерения и расположение итогового деления на `Offered_QTY`, поэтому её нельзя безопасно исполнять по документу.

## Открытые вопросы для утверждения

1. Каковы точные правила автоматических FCL/LCL-формул Airtable?

## Источники

- [[projects/svmpx/04-source-register/sources/supporting/operations/ddp-logic]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-card]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-status-errors]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-overview]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-card]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow]]
- [[projects/svmpx/04-source-register/sources/supporting/operations/sda-master-sample]]
