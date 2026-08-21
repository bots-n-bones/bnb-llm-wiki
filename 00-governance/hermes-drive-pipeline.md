---
schema: hermes-kb/v2
id: kb-v2-hermes-drive-pipeline
title: Hermes Drive-to-Wiki pipeline
project: shared
type: policy
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Операционный контур Drive Inbox → источники → Wiki → локальный индекс Hermes.
source_ids: [src-local-bnb-project-manifest]
created: 2026-08-21
updated: 2026-08-21
tags: [hermes, google-drive, inbox, curation, index]
---

# Hermes Drive-to-Wiki pipeline

## Runtime boundary

Hermes answers from the server-local SQLite index. Google Drive is never a
per-question full-text backend. Drive holds originals, media, working files and
the project Inbox; GitHub holds the curated Wiki revision; the server index is
an atomically replaceable derived artifact.

## Intake

New material arrives through an authorized Hermes request or the canonical
Drive `00 - inbox` folder. The processor classifies project and confidentiality,
records the original file identifier/path/time, extracts readable text when
appropriate, and creates a source record plus a draft. A user message or a
fresh file alone cannot create active canon.

## Curation and release

The pipeline validates metadata, provenance, links, lifecycle and secrets;
records unresolved issues in the owner review queue; then publishes a validated
Wiki revision. The server synchronizes that revision, rebuilds the local FTS
index and performs a retrieval smoke test before replacing its current index.

## Authority

Answers prefer `active-canonical`. Active sources may provide evidence but not
override canon. Draft, historical, archived and quarantined material must be
labeled. Owner approval is required for canonical promotion, destructive work,
external publishing, purchases and financial actions.
