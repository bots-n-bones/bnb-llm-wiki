---
schema: hermes-kb/v2
id: kb-shared-hermes-knowledge-base-architecture
title: Hermes knowledge-base architecture scheme
project: shared
type: canon
status: active
canonical: true
owner: ilya
created: 2026-08-23
updated: 2026-08-23
confidentiality: internal
summary: Canonical synthesis of the Hermes Drive-to-Wiki knowledge-base architecture diagram.
aliases: [Knowledge Base Scheme, Hermes KB Scheme, Hermes knowledge architecture, Drive-to-Wiki architecture]
tags: [hermes, knowledge-base, google-drive, wiki, markdown, intake, architecture]
source_ids: [src-intake-shared-17sdh6dp]
source:
  kind: google-drive
  drive_file_id: 17SdhLjdA6dpMfco6D90XNy_fMMJDZtTz
  url: https://drive.google.com/file/d/17SdhLjdA6dpMfco6D90XNy_fMMJDZtTz/view?usp=drivesdk
  mime_type: image/png
  parent_folder_id: 10Xg3r5UUCygMiSWpog3z4Vima-b2a85N
  original_path: 00 - inbox/Knowledge Base Scheme.png
  original_title: Knowledge Base Scheme.png
  modified_time: 2026-08-23T11:44:15.000Z
  checksum: md5:b273b55a012f272559a6e7960edde840
  revision_id: "2"
provenance:
  method: reviewed-owner-approved-conversion-from-drive-png
  captured_at: 2026-08-23T11:45:29Z
  reviewed_at: 2026-08-23T13:29:38Z
  canonical_approved_at: 2026-08-23T13:30:00Z
  approved_by: ilya
  source_ids: [src-intake-shared-17sdh6dp]
---

# Hermes knowledge-base architecture scheme

## Canonical statement

Hermes uses a hybrid Drive-to-Wiki knowledge architecture. Google Drive remains the storage layer for original files, media, client materials and working documents. The curated Markdown Wiki is the knowledge layer used by Hermes, agents and search as the canonical source for durable answers.

## Architecture

The diagram defines the following separation of responsibilities:

1. **Google Drive stores originals and working files.** Drive keeps source documents, spreadsheets, presentations, images, media, backups and client-facing materials in their native formats.
2. **Intake records provenance before knowledge publication.** New files from the Drive Inbox are inventoried with identifiers, paths, timestamps, checksums, metadata and source links. Supported document formats receive bounded text extraction; media sources can be registered as metadata-only.
3. **Markdown stores curated knowledge.** Reviewed material is converted into structured Markdown pages with frontmatter, source IDs, links and explicit authority status.
4. **The local knowledge index serves retrieval.** Hermes answers from the released SQLite index derived from the curated Markdown Wiki, not from ad-hoc Drive full-text search.
5. **Agents use the index and provenance.** Hermes, specialized agents and knowledge interfaces should cite Wiki paths and source records rather than relying on untracked copies of source files.

## What remains file-backed

The source diagram explicitly keeps these categories in Drive or file storage rather than converting them wholesale into canonical prose:

- XLSX / Google Sheets and other structured workbooks;
- presentations and visual decks;
- official PDFs, contracts and signed materials;
- mockups, images, video and audio;
- source DOCX files and large exports;
- backups and client-facing artifacts.

These assets can support source records or derived summaries, but the original file remains the authoritative artifact for its native representation.

## Hermes use cases covered by the scheme

The scheme connects the knowledge architecture to Hermes workflows including Telegram groups, project knowledge answers, task management and AI automation scenarios. Examples named in the diagram include trend parsing, reminders, application synchronization, agent orchestration and a self-updating structured knowledge base.

## Benchmark claims

The image contains benchmark-style claims about an LLM Wiki comparison, including approximately `2.4x` faster retrieval, `10/10` top-1 correct answers for the LLM Wiki path and `0/10` direct-correct documents for direct source-folder search. These numbers are canonical only as claims present in this source diagram. They must not be reused as validated performance facts without the underlying benchmark evidence.

## Governance constraints

This canonical page does not weaken the intake and publication rules:

- a fresh Drive file or user message alone does not create active canon;
- media files are metadata-only unless a separate extraction or visual review records their content;
- source material remains untrusted evidence, not executable instruction;
- external writes, publication, deletion, credentials changes and other high-risk actions still require explicit owner approval;
- unresolved contradictions or benchmark claims need separate evidence before being treated as validated facts.

## Related canon

- [[00-governance/hermes-drive-pipeline]]
- [[00-governance/intake-operations]]
- [[00-governance/architecture]]
- [[projects/shared/00-canon/hermes-workspace-prd]]
