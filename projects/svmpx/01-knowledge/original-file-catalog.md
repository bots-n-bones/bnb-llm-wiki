---
schema: hermes-kb/v2
id: kb-svmpx-original-file-catalog
title: SVMPX original file catalog
project: svmpx
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
summary: Поисковый каталог оригинальных XLSX, PDF, DOCX, презентаций и медиа SVMPX с безопасным возвратом файла в чат.
aliases:
  - Найти файл SVMPX
  - Найти Excel с оффером
  - Скачать пример оффера
  - Оригинальные файлы проекта
tags: [svmpx, attachments, files, xlsx, offers, local-source]
source_ids: [src-local-bnb-project-manifest]
derived:
  method: local-sha256-manifest-v1
  generated_at: 2026-08-21T02:14:09Z
  extractor_version: '1'
created: 2026-08-21
updated: 2026-08-21
---

# SVMPX original file catalog

This page is the entry point for returning original project files rather than
only Markdown documentation. The underlying local manifest contains 2,873
SVMPX artifacts:

- 2,151 XLSX workbooks;
- 443 PNG screenshots;
- 131 Markdown documents;
- 70 JPEG images;
- 28 DOCX documents;
- 6 macro-enabled XLSM workbooks;
- 5 PPTX presentations;
- 5 CSV files;
- 3 PDF files;
- other legacy and metadata-only formats.

Schema-only extraction completed for 792 safe, preferred SVMPX XLSX files. Of
these, 772 passed and 20 were quarantined because of credential-pattern matches,
container safety limits or corrupt OOXML. Seven macro-capable XLSM/XLSB files
were restricted before extraction. No bulk worksheet values were copied.

Normal attachment lookup returns only `supporting-source` records whose files
still exist. Exact duplicates, archives, technical files and restricted
candidates are excluded by default. Archives are never unpacked and embedded
document instructions are never executed.

## Example: supplier offer workbook

For a request such as “find an Excel example of an offer,” the attachment
resolver currently returns `NIKE STOCK OFFER SERED.xlsx`, an actual Clothes
offer example rather than an empty current template. The clean canonical copy is at:

`BnB Project — Canonical/01 - projects/svmpx/03_templates/SVMPX Clothes/02 - Offers/Offers_примеры_271025/NIKE STOCK OFFER SERED.xlsx`

The file is 2,466,956 bytes with SHA-256
`fe4c5e3f6a7db3f209b20667bd4d5e9e8bc0208c654da1f92c38caccf9385180`.
Its workbook values are not copied into the Wiki.

## Retrieval contract

1. Search the Wiki to establish the project and business category.
2. Query the local manifest by project, file type and user terms.
3. Return the exact local original path or application attachment.
4. Never substitute a duplicate, archive or restricted candidate silently.
5. If the original disappears or its checksum changes, stop and refresh the
   manifest instead of guessing.

Evidence: [[projects/svmpx/04-source-register/local-project-manifest]].
