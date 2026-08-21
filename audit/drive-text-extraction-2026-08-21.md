---
schema: hermes-kb/v2
id: audit-drive-text-extraction-2026-08-21
title: Drive text extraction coverage — 2026-08-21
project: shared
type: index
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Полная выгрузка доступного текстового слоя шести проектных папок Google Drive.
created: 2026-08-21
updated: 2026-08-21
tags: [audit, google-drive, extraction, coverage]
---

# Drive text extraction coverage — 2026-08-21

## Scope and result

Read-only extraction traversed all portable text files and native Google
documents/sheets under `01 - projects` for `bots-n-bones`, `content-os`,
`hello i am`, `quntm`, `svmpx` and `ursus`. It fetched Markdown, JSON, CSV,
plain text, Google Docs and native Google Sheets through the connected Drive
account. The run completed without access errors.

| Measure | Result |
| --- | ---: |
| Candidate files fetched | 1,129 |
| Non-empty text extractions | 745 |
| Extracted characters | 4,855,737 |
| Connector access errors | 0 |

## Useful extracted material by project

| Project | Non-empty files | Characters | Note |
| --- | ---: | ---: | --- |
| Content OS | 581 | 3,667,781 | Includes source material, duplicate development exports and vendored dependencies; only governed project material is eligible for knowledge pages. |
| SVMPX | 125 | 939,594 | Includes documentation, operations drafts, exports and repeated file-catalog snapshots. |
| Hello I Am | 34 | 225,018 | Brand, editorial, production and analytics material. |
| Bots-n-Bones | 3 | 13,351 | Case documentation and an access/automation model. |
| Quntm | 2 | 9,993 | Case material and services-question draft. |
| Ursus | 0 | 0 | No readable text returned in the selected Drive formats. |

## Handling policy

This run proves that the text was available and successfully read; it does not
make every source canonical. Raw Drive content stays in its original Drive file.
The Wiki receives only a source record and a reviewable derived page when the
material has a clear project scope and can be cited. Duplicated exports,
`node_modules`, third-party notices and generated caches are excluded from
knowledge claims.

Binary media and large office artifacts remain represented by Drive inventory
metadata. They are not OCRed or treated as textual evidence until a project use
case requires that work.

## Next extraction lane: workbook evidence

The inventory has 2,156 stored XLSX workbooks (about 273 MB). Most are SVMPX
operational samples or repeated export packages: four directory exports repeat
the same Source Offer, Client Proposal, Shipment and Product sets. They are
not bulk-indexed as independent facts. The next pass deduplicates them by
content-bearing export role and extracts high-value unique workbooks, beginning
with the DDP/landed-cost workbook recorded at
[[projects/svmpx/04-source-register/sources/supporting/operations/sda-master-sample]].
