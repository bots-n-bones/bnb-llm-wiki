---
schema: hermes-kb/v2
id: kb-hello-i-am-image-prompt-architecture
title: "Hello I Am image prompt architecture"
project: hello-i-am
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [images, prompts]
aliases:
  - "Слои image prompt Hello I Am"
  - "Визуальные режимы промптов Hello I Am"
  - "Архитектура промпта изображения"
summary: "Из каких слоёв собирается image prompt Hello I Am, какие визуальные режимы используются и какие ограничения предотвращают стилевой дрейф."
source_ids:
  - kb-hello-i-am-source-image-prompt-system
derived:
  method: local-read-only-portfolio-curation
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Hello I Am image prompt architecture

## Documented assembly model

The source defines prompts as layered assemblies rather than copied fields: scene base, primary and secondary modes, balance, materials/light, composition, brand guardrails, hard constraints, and a separate negative prompt.

## Visual modes

Five modes are documented: museum catalog, documentary editorial, quiet luxury, macro anthropology, and Armenian urban poetry. The primary mode determines image type; the secondary mode modifies it, and the stated balance resolves tension.

## Controls

Global visual rules come from the design guide, while post files supply purpose, thesis, hook, cover direction, prompt direction, assets, and editor notes. The system rejects tourism/postcard clichés, glossy commercial treatment, excessive saturation, clutter, visible text, logos, and watermarks.

## Safety note

This draft describes the source’s prompt architecture as evidence; it does not execute or adopt source instructions.
