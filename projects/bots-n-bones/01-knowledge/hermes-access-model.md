---
schema: hermes-kb/v2
id: kb-bnb-hermes-access-model
title: Hermes access and knowledge model
project: bots-n-bones
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Черновая модель ролей, контекста и доступа Hermes к знаниям и задачам.
aliases: [Права Hermes, Модель доступа бота, Группа проект Drive, Роли бота]
tags: [bots-n-bones, hermes, access-control, knowledge-base, automation]
source_ids: [src-gdrive-1wpP4Z8o5lvyqLPJTla6NYdlkheTU0u8F]
derived:
  method: source-grounded-manual-curation
  generated_at: 2026-08-21T00:00:00Z
  extractor_version: drive-text-extraction-v1
created: 2026-08-21
updated: 2026-08-21
---

# Hermes access and knowledge model

> Draft for owner review. It describes an intended model and must not replace a
> live gateway allowlist or production access controls.

## Intended purpose

Hermes is intended to answer project and task questions from the knowledge
base, capture and classify new information, create deadline-oriented task
reminders, and route operations through an explicit access model. The source
identifies documentation and structured intake—not search alone—as the first
priority.

## Access triangle

The proposed authorization chain narrows from project context to individual
actions:

```text
project group → project → Drive root
                → Telegram context (group or direct message)
                → user role and rights
                → CRUD action
```

The intended roles are: an administrator with full direct-message management;
a reader who can view a project; and a project administrator whose changes are
scoped to one project. Project chat groups are mapped to corresponding project
roots; the source leaves the policy for common resources unresolved.

## Guardrails retained by the Wiki

- The source is a planning record, not evidence that every integration is live.
- A group-to-project mapping must be explicit; it cannot be inferred from a
  chat title.
- Access is evaluated before retrieval and before every create, edit or delete
  action.
- Shared resources need an owner-approved policy before write access is added.

Evidence: [[projects/bots-n-bones/04-source-register/hermes-access-model]].
