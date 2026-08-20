---
schema: hermes-kb/v2
id: source-register-svmpx
title: SVMPX Source Register
project: svmpx
type: index
domain: sources
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Реестр происхождения сведений и исходных материалов SVMPX, включая источники из Telegram, Notion и Google Drive.
aliases:
  - Источники SVMPX
  - Происхождение сведений Telegram и Notion
created: 2026-08-19
updated: 2026-08-19
tags: [svmpx, sources, provenance]
---

# SVMPX Source Register

This register contains one Markdown record per material source or logical source
package. Raw files remain on Google Drive.

## Verified roots

- Primary immutable source candidate: [shared SVMPX root](https://drive.google.com/drive/folders/1xPXXJGy96dEsQkMoAHWQ3MVluSup0-YC)
  (`1xPXXJGy96dEsQkMoAHWQ3MVluSup0-YC`).
- Bulk copy created 2026-08-18: [SVMPX copy](https://drive.google.com/drive/folders/1esqsHWpJYEUSPwSJV0BHOcMJnoguHYfZ)
  (`1esqsHWpJYEUSPwSJV0BHOcMJnoguHYfZ`).
- Partial bulk copy created 2026-08-19: [SVMPX partial copy](https://drive.google.com/drive/folders/1jBlEykNey1awW_aA5U1IZ9Eeod_-Q-cB)
  (`1jBlEykNey1awW_aA5U1IZ9Eeod_-Q-cB`).

The primary root is a candidate, not yet a human-approved canonical source. The
August roots remain duplicate candidates until the full manifest comparison is
complete. Nothing is deleted or moved.

## Registration states

- `discovered` — present in inventory, not yet classified.
- `candidate` — potentially relevant to the canonical KB.
- `registered` — provenance and owner captured.
- `processed` — derived representation generated and checked.
- `canonical-source` — approved primary evidence for current knowledge.
- `quarantined` — duplicate, obsolete, or uncertain; retained without deletion.

## Registered pilot sources

- [[projects/svmpx/04-source-register/sources/source-register|Legacy source register]]
- [[projects/svmpx/04-source-register/sources/master-index|Legacy master index]]
- [[projects/svmpx/04-source-register/sources/system-documentation-map|System documentation map]]
- [[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion full export map]]
- [[projects/svmpx/04-source-register/sources/documentation-index|Operational documentation index]]
- Supporting source records used by the canonical drafts:
  - `sources/supporting/core/` — project map and system specification.
  - `sources/supporting/operations/` — bot, status, message, and DDP evidence.
  - `sources/supporting/quality/` — test protocol, automation inventory, and historical roadmap.
- [[projects/svmpx/04-source-register/dedupe-report|Partial-evidence dedupe report]]

See [[audit/drive-baseline-summary-2026-08-19]].

## Telegram and Notion provenance

Legacy Notion exports are registered through
[[projects/svmpx/04-source-register/sources/notion-full-export-map]]. Telegram
bot evidence is registered through the restricted
[[projects/svmpx/04-source-register/sources/supporting/operations/tg-chatbots]].
That source contains plaintext bot credentials in Drive; no credential value
is copied into this repository or indexed by Hermes. The tokens require
rotation and storage in a secret manager.
