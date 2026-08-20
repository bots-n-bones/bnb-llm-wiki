---
schema: hermes-kb/v2
id: kb-svmpx-qa-protocol
title: SVMPX QA Protocol
project: svmpx
type: canon
domain: quality
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: "Черновой протокол тестирования сценариев Electronics и Clothes, ручных проверок, автоматизации и критериев приёмки."
aliases:
  - Протокол тестирования SVMPX
  - Тестирование Electronics и Clothes
tags: [svmpx, qa, testing, acceptance]
source_ids:
  - src-gdrive-128gJBYslTAfRRtHsxIHTEmVoTTpUbtxuhtEYXCpTdIY
  - src-gdrive-1ImiLnOXLysLgprKDYZhvVbiqQp2n3UP4kdHWYcfcH88
  - src-gdrive-1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4
related:
  - projects/svmpx/00-canon/project-overview
  - projects/svmpx/00-canon/system-documentation
  - projects/svmpx/00-canon/data-model
  - projects/svmpx/00-canon/bot-scenarios
  - projects/svmpx/00-canon/ddp-finance-flow
created: 2026-08-19
updated: 2026-08-20
---

# SVMPX QA Protocol

## Решения владельца

Авторитетной целью приёмки является production Airtable-база. Electronics и
Clothing должны иметь одинаковую функциональность, кроме утверждённого правила
поставщиков: Electronics PO может включать нескольких поставщиков, Clothing PO
— только одного. Финальное QA и выпуск изменений утверждает Илья.

В текущей практике выпуск блокируют критические ошибки. Тестовые логи,
автоматические тесты и отдельно сохранённые тестовые файлы отсутствуют. AI для
обработки офферов не используется. Проверки, включая опасные операции,
выполняются на обычных production-данных. Это описание текущего состояния, а не
рекомендуемый безопасный QA-процесс.

## Зафиксированный риск production-тестирования

Проверка удаления и других разрушительных операций на обычных production-данных
может необратимо изменить рабочую информацию. До автоматизации таких сценариев
нужны изолированные тестовые записи, резервное копирование и проверяемый cleanup
или rollback. Hermes не должен самостоятельно запускать destructive QA в
production.

Владелец подтвердил сохранение этой практики без выделенных тестовых записей и
rollback. Риск принят, но он не даёт Hermes разрешения выполнять destructive
операции: такие проверки остаются только ручным действием ответственного
человека.

This page is a draft. It converts historical checklists into a proposed QA
contract without treating checked boxes or document names as current execution
evidence.

## Confirmed from sources

### Manual coverage inventory

The legacy [SVMPX Test Protocol](https://docs.google.com/document/d/128gJBYslTAfRRtHsxIHTEmVoTTpUbtxuhtEYXCpTdIY/edit)
contains an unchecked manual checklist for both Electronics and Clothes. Its
coverage includes:

- product ingestion from Telegram and creation through the interface;
- offer ingestion, interface presentation, and offer-related AI behavior;
- client proposal creation, DDP calculation, Proposal Lines, generated files,
  deletion, and selected-offer behavior;
- order creation from Telegram, deletion, and creation of inbound and outbound
  shipments;
- shipment creation from a file, flags, deletion, and a five-shipment check.

Because every item in that source is unchecked, the document confirms intended
coverage only. It does not prove that any scenario passed.

Registered provenance:
[[projects/svmpx/04-source-register/sources/supporting/quality/test-protocol|SVMPX Test Protocol source record]].

### Historical automation inventory

The legacy [SVMPX Automation Tests](https://docs.google.com/document/d/1ImiLnOXLysLgprKDYZhvVbiqQp2n3UP4kdHWYcfcH88/edit)
marks items as completed for product and offer ingestion, proposal comments and
email delivery, notifications and proposal logging, parsing, and several
Airtable automations. One min/max/average update is explicitly described as no
longer needed. The final `AI` heading has no documented checks beneath it.

These checkmarks are historical source claims, not reproducible test results.
The source provides no execution date, environment, build identifier, logs, or
failure evidence.

Registered provenance:
[[projects/svmpx/04-source-register/sources/supporting/quality/automation-tests|SVMPX Automation Tests source record]].

### Documentation available for scenario design

The registered operational source set covers 21 Markdown documents across
products, source offers, client proposals, purchase orders, and shipments. It
is indexed in
[[projects/svmpx/04-source-register/sources/documentation-index|the operational documentation index]]
and is explicitly non-canonical pending implementation verification. The
[[projects/svmpx/04-source-register/sources/system-documentation-map|system documentation map]]
also lists QA as part of the intended system documentation scope.

## Proposed QA contract

### Required evidence for every run

Record the following before a result can be accepted:

- test case ID and business flow;
- Electronics or Clothes scope;
- environment and build or revision identifier;
- input fixture or source file;
- expected and actual result;
- pass, fail, blocked, or not-run status;
- timestamp, executor, and links to logs or screenshots;
- created or changed record IDs so side effects can be inspected and cleaned up.

Historical checkmarks without this evidence should remain `unverified`.

### Proposed release gates

1. **Ingestion smoke:** create products and offers through each supported entry
   path; verify validation, duplicate behavior, logs, and user-visible result.
2. **Commercial flow:** create a client proposal from selected offers; verify
   Proposal Lines, DDP values against an approved fixture, generated file,
   comments, and delivery behavior.
3. **Order and logistics flow:** create an order and inbound/outbound shipments;
   verify templates, links, flags, and deletion behavior.
4. **Automation regression:** execute each automation still classified as
   active and attach reproducible evidence. Retired automations are excluded by
   an explicit decision, not by omission.
5. **Cross-domain parity:** run the approved matrix separately for Electronics
   and Clothes; do not infer Clothes behavior from an Electronics pass.
6. **Acceptance:** a release candidate has no unresolved critical flow failure,
   and every blocked or excluded check has an owner and decision record.

Exact severity definitions and release thresholds remain unresolved below; the
last gate therefore cannot yet be used as a final approval policy.

### Proposed source-to-test traceability

Test cases should cite the relevant operational source record and related canon
page. Initial traceability anchors are:

- [[projects/svmpx/00-canon/data-model|Data model]] for entities, required
  fields, and relationships;
- [[projects/svmpx/00-canon/bot-scenarios|Bot scenarios]] for Telegram inputs,
  notifications, and user-facing failures;
- [[projects/svmpx/00-canon/ddp-finance-flow|DDP and finance flow]] for approved
  calculation fixtures;
- [[projects/svmpx/00-canon/system-documentation|System documentation]] for
  integration boundaries and observable side effects;
- [[projects/svmpx/00-canon/project-overview|Project overview]] for scope and
  terminology.

## Accepted limitations

- Wiki intentionally has no numeric DDP fixture or calculator.
- QA has no automated tests, durable test logs, or stored fixtures.
- Production-data testing remains an owner-accepted operational risk.
- Hermes must not initiate destructive production tests.
