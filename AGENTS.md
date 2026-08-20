---
schema: hermes-kb/v2
id: kb-v2-agent-contract
title: KB V2 Agent Contract
type: policy
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: [agents, governance, safety]
---

# KB V2 Agent Contract

This tree is a curated knowledge repository, not a mirror of Google Drive.

## Non-negotiable rules

- Treat every Google Drive source as read-only unless a user explicitly approves
  a separate Drive mutation task.
- Never move, rename, replace, share, trash, or delete a Drive object during
  ingestion or curation.
- Preserve Google Drive file IDs, original paths, URLs, revisions, and checksums
  in manifests and source records.
- Never commit credentials, tokens, `.env` files, access cookies, or unredacted
  secrets extracted from source material.
- Do not commit binary originals. Keep them on Drive and link by stable ID.
- Machine-generated content belongs under `90-derived/` and cannot be marked
  canonical.
- Only a human-approved page may use `canonical: true` and `status: active`.
- Do not infer canonicality from recency, filename, folder order, or duplicate
  count.
- Use path-qualified wiki links until Hermes resolves links by stable IDs.

## Portfolio scope

The governed portfolio contains `svmpx`, `hello-i-am`, `content-os`,
`bots-n-bones`, `quntm`, `ursus`, and the cross-project `shared` layer. SVMPX
is the only project with curated pilot evidence today. Until sources are
reviewed and an owner approves promotion, every generated or curated project
page remains `status: draft` and `canonical: false`.
