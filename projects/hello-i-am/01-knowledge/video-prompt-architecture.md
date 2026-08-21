---
schema: hermes-kb/v2
id: kb-hello-i-am-video-prompt-architecture
title: "Hello I Am video prompt architecture"
project: hello-i-am
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [video, prompts]
aliases:
  - "Hero prompts style lanes и category rollups Hello I Am"
  - "Архитектура видео-промптов Hello I Am"
  - "Геройские промпты стилевые линии и роллапы категорий"
summary: "Как устроены hero prompts, style lanes и category rollups для видео Hello I Am, включая слоты, инварианты и проверки."
source_ids:
  - kb-hello-i-am-source-video-prompt-system
derived:
  method: local-read-only-portfolio-curation
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Hello I Am video prompt architecture

## Hero-prompt model

The source uses one shared master template plus one item-specific scene line for each leaf item. The MVP prioritizes one hero prompt per item before additional texture, ritual, ambience, and reveal slots.

## Style lanes

Five lanes are documented: museum catalog, documentary editorial, urban poetry, macro anthropology, and soundscape. All share vertical editorial pacing, warm neutral light, tactile surfaces, restrained camera movement, and a ban on visible text/logos and tourism-style presentation.

## Rollups and validation

After several leaf posts in an area, a separate category-map rollup is produced; it is not a concatenation of leaf prompts. Validation expects consistent outputs from the same item row, cross-item brand coherence, recognizable category maps, and no drift into tourism or food-commercial language.

## Safety note

This is documentation of the source system only; no prompt or external generation command was executed.
