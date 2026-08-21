---
schema: hermes-kb/v2
id: kb-shared-agent-team-practices
title: Agent team coordination practices
project: shared
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Черновая выжимка внешних рекомендаций по ownership, размеру задач и quality gates.
aliases: [Правила agent teams, Ownership и quality gates, Координация агентов]
tags: [shared, agents, coordination, quality, ownership]
source_ids: [src-local-shared-agent-teams-e9b94a3a]
created: 2026-08-20
updated: 2026-08-20
---

# Agent team coordination practices

Внешний набор рекомендует одну ясную deliverable и один набор файлов на задачу.
Для параллельной работы описаны pipeline, fan-out, fan-in и diamond. Ключевое
правило ownership: один исходный файл одновременно принадлежит одному агенту;
общие конфиги закрепляются за lead или одним назначенным владельцем.

Перед завершением предлагаются gates: тесты, lint, ручная проверка при
отсутствии тестов, сверка acceptance criteria и отсутствие частичных TODO.
Обычные сообщения адресуются конкретному участнику; broadcast оставляется для
критических проблем всей команды.

Эти положения не переопределяют `AGENTS.md`, `swarm.yaml` или роли Hermes.

Evidence: [[projects/shared/04-source-register/agent-teams-directory]].
