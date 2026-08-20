---
schema: hermes-kb/v2
id: kb-v2-lifecycle
title: KB V2 Lifecycle and Rollback
type: policy
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: [migration, rollback, governance]
---

# KB V2 Lifecycle and Rollback

## Pilot phases

1. Inventory source metadata without Drive mutations.
2. Register sources and detect duplicate candidates.
3. Extract derived text without changing originals.
4. Curate and approve canonical Markdown.
5. Point a test Hermes configuration at KB V2.
6. Accept the pilot before any legacy cleanup is proposed.

## Rollback

Rollback means disconnecting KB V2 from Hermes and returning to the previous
knowledge source. Because the legacy Drive tree is not changed during the pilot,
no restore operation is required for source files.

No duplicate candidate may be deleted until its file ID, parents, metadata,
checksum or revision, canonical replacement, and approver are captured in an
accepted audit report.
