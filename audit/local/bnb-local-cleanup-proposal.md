---
schema: hermes-kb/v2
id: audit-bnb-local-cleanup-proposal-2026-08-21
title: BnB local cleanup proposal
type: reference
status: active
canonical: false
owner: ilya
confidentiality: internal
summary: Безопасный план объединения скачанных фрагментов BnB без удаления исходников и без выбора бизнес-канона по имени файла.
created: 2026-08-21
updated: 2026-08-21
tags: [audit, cleanup, deduplication, local-source]
---

# BnB local cleanup proposal

## Confirmed automatically

- The downloaded root contains 11,854 files and 6,948,850,676 bytes.
- 846 exact SHA-256 duplicate groups contain 3,317 members.
- Exact duplicates account for 597,730,320 redundant bytes.
- 6,687 files are technical or explicitly excluded from indexing, primarily
  dependencies, build artifacts, caches, temporary files and environment
  examples.
- 396 files are archive-only. No archive was extracted.
- 8 files are restricted: seven macro-capable SVMPX spreadsheets and one text
  source containing a credential pattern. Secret values are not recorded here.
- 3,057 files remain preferred supporting-source candidates after exact-dedup,
  safety and technical filters.

## Why the three roots cannot simply be deleted

The roots are fragments, not identical backups. For SVMPX alone:

| Root             | Files | Unique content hashes | Hashes exclusive to that root |
| ---------------- | ----: | --------------------: | ----------------------------: |
| `bots-n-bones`   |   876 |                   607 |                           335 |
| `bots-n-bones 2` | 1,458 |                   762 |                           455 |
| `bots-n-bones 3` |   539 |                   299 |                            61 |

Deleting either root wholesale would lose unique files. The safe canonical
assembly is therefore the union of preferred checksum records, not one chosen
download folder.

## Spreadsheet processing

Schema-only extraction ran for 803 safe preferred XLSX files across the
portfolio. It produced sheet counts, sheet names, used ranges, headers and
formula patterns without copying bulk row values. 783 workbooks passed; 20 were
quarantined because of secret-pattern matches, unsafe container limits or
corrupt OOXML. SVMPX accounts for 792 processed workbooks: 772 passed and 20
were quarantined.

## Proposed physical cleanup, not yet executed

1. Create a new `BnB Project — Canonical` directory from the union manifest.
2. Preserve the current downloaded roots unchanged as rollback evidence.
3. Materialize only preferred supporting sources into the clean taxonomy.
4. Put exact duplicates in a review manifest rather than copying them.
5. Keep archives in `99 - archive` and restricted files in `99 - quarantine`.
6. After user acceptance and a second checksum verification, archive the three
   old fragments; do not permanently delete them during the first release.

No physical move, rename or deletion has been performed.
