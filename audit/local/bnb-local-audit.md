---
schema: hermes-kb/v2
id: audit-bnb-local-2026-08-21
title: BnB local project audit
type: reference
status: active
canonical: false
owner: ilya
confidentiality: internal
created: 2026-08-21
updated: 2026-08-21
tags: [audit, local-source, deduplication]
---

# BnB local project audit

Read-only inventory of the downloaded BnB project. No source file was moved, renamed, deleted, opened as an application, or extracted from an archive. Checksums are content hashes, not business approval.

- Files: **11,854**
- Bytes: **6,948,850,676**
- Exact duplicate groups: **846**
- Files participating in exact duplicate groups: **3,317**
- Redundant bytes represented by exact duplicates: **597,730,320**
- Same logical path with different content: **0**

## Classification

- archive-only: 396
- duplicate-candidate: 1,706
- out-of-scope: 6,687
- restricted: 8
- supporting-source: 3,057

## Safety and interpretation

- Duplicate status is based only on identical SHA-256 content.
- A preferred candidate is a deterministic review suggestion, not an approved deletion target.
- Archives were not extracted.
- Files with secret-like names are restricted candidates and must not enter the search index.
- Business-level near-duplicates and superseded versions still require semantic review.
