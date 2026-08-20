---
schema: hermes-kb/v2
id: kb-shared-event-driven-agents
title: Event-driven multi-agent patterns
project: shared
type: research
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Черновая выжимка внешней публикации о streaming-based coordination агентных систем.
aliases: [Event-driven агенты, Событийные multi-agent паттерны, Orchestrator-worker recovery]
tags: [shared, agents, event-driven, architecture, research]
source_ids: [src-local-shared-event-agents-350c185c]
created: 2026-08-20
updated: 2026-08-20
---

# Event-driven multi-agent patterns

> Внешняя публикация поставщика платформы; не архитектурное решение Hermes.

Источник противопоставляет синхронный request/response событийной координации,
где агенты потребляют и публикуют события асинхронно. Он выделяет четыре
multi-agent pattern:

- **orchestrator-worker:** команды распределяются по partitions, workers
  работают как consumer group, результаты уходят в отдельный topic;
- **hierarchical:** каждый не-листовой агент оркестрирует своё поддерево через
  события;
- **blackboard:** общая память представлена event stream, на обновления которой
  подписываются агенты;
- **market-based:** offers/requests публикуются как события, а matching service
  сводит их без прямых peer-to-peer соединений.

Заявленные преимущества — replay, consumer rebalancing, горизонтальное
масштабирование, fault isolation и свежие данные. Практики вроде idempotent
processing и dead-letter queues представлены как способы безопасного retry и
human oversight. Применимость к Hermes должна подтверждаться отдельным ADR.

Evidence: [[projects/shared/04-source-register/event-driven-agents-pdf]].
