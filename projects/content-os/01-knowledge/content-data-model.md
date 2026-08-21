---
schema: hermes-kb/v2
id: kb-content-os-content-data-model
title: "Content OS reference data model"
project: content-os
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [data-model, airtable]
aliases:
  - "Сущности и связи data model Content OS"
  - "Reference data model ContentOS"
  - "Таблицы и отношения Airtable Content OS"
summary: "Основные сущности и связи reference data model Content OS: products, generated content, platforms, posts, campaigns, talents, people и prompts."
source_ids:
  - kb-content-os-source-database-schema
  - kb-content-os-source-airtable-relations
derived:
  method: local-read-only-portfolio-curation
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Content OS reference data model

## Main entities

The referenced schema includes Settings, Products, Generated Content, Platforms, Social Posts, Campaigns, Talents, People, Prompt Templates, Inspiration, External Automations, and Content Templates, plus analytics-oriented entities.

## Core relationships

Products and brands connect to generated assets and social posts. Generated Content links products, prompt templates, inspirations, talents, creators, approvers, and automation phases. Platforms host social posts; campaigns group posts and metrics; people create, approve, and manage work.

## Lifecycle fields

Generated Content has draft-to-published style statuses and automation triggers/phases. Social Posts has draft, scheduled, published, rejected, and archived states. Campaigns carry goals, budgets, dates, objectives, KPIs, managers, and status.

## Confidence boundary

The relation map was reconstructed from linked-record fields. Some edges are explicitly inferred from field names and require verification against the live database.
