---
schema: hermes-kb/v2
id: audit-drive-svmpx-baseline-2026-08-19
title: SVMPX Drive Baseline Summary
project: svmpx
type: reference
domain: audit
status: active
canonical: false
owner: codex
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: [svmpx, drive, audit, dedupe]
---

# SVMPX Drive Baseline Summary

This is a verified structural baseline, not yet the complete recursive JSONL
manifest. Google Drive was read-only during discovery.

## Verified coverage

- 86 folders opened recursively to depth 4.
- 1,466 objects discovered: 180 folders and 1,286 files.
- Approximately 589 MB from available file sizes.
- 877 XLSX, 1 CSV, 66 Markdown, 23 Google Docs, 3 DOCX, 289 images,
  1 PDF, 1 MP4, and 1 PPTX, plus archive and technical formats.
- No opened folder reached the 1,000-child connector limit.
- Folders first discovered at depth 4 were not expanded, so these values remain
  a verified lower bound rather than Gate 0 completeness.

Duplicate indicators inside the source root:

- 119 normalized-name groups containing 263 files.
- 67 probable exact groups by normalized title, logical type, and size,
  containing 147 files.

## Root comparison

| Role | Drive ID | Created/observed | Verified direct folders | Assessment |
|---|---|---:|---:|---|
| Shared source candidate | `1xPXXJGy96dEsQkMoAHWQ3MVluSup0-YC` | 2026-04-15 onward | 9 | Most complete and oldest verified root |
| Bulk copy | `1esqsHWpJYEUSPwSJV0BHOcMJnoguHYfZ` | 2026-08-18 | 8 | Missing `08_meetings`; duplicate candidate |
| Partial bulk copy | `1jBlEykNey1awW_aA5U1IZ9Eeod_-Q-cB` | 2026-08-19 | 3 | Only data, templates, and old Notion export |

## Primary source candidate tree

- `00_data` — `1dhGy6U1pfL9t-FMDTQly_puJrM204ojJ`
- `01_documentation` — `1hHr0oO0Ua2R96wM_hVb2n0SDD419-N0n`
- `02_screenshots` — `1nPB18AwoyKMkCHfg985C5Z_8YvX2N9uu`
- `03_templates` — `1d2GdJbITgCIjfMBtHU-fJvjWqT9NQ3T9`
- `04_ideas` — `1Kt8Z0IeZFNJBzh-SrQ8lwEJkrCNLdFfO`
- `05_backups` — `1167hsf8s--ryPbT3-jxA5PS74JN4JsvF`
- `06_old_notion` — `1Wm4R09SZsO1cnyhTtROhk1VOjy3nHkmG`
- `07_links` — `1bAdWY51KmYMCxTOQag51gBNjMV6_vyGt`
- `08_meetings` — `11fqPk8s8Gf3oBlxYyeAZ5ydG__VdIBTZ`

## Current decision

Use the shared root as the immutable ingestion scope for the pilot. Treat both
August roots as duplicate candidates. This recommendation must not be interpreted
as permission to delete or reorganize them.

## Coverage limitation

The connected Drive folder listing returns at most 1,000 direct children and does
not expose a folder-list pagination cursor. Any folder at that boundary must be
marked `partial` in the machine manifest and audited through a paginated metadata
search or a dedicated readonly ingestion service before Gate 0 can pass.

See [[projects/svmpx/04-source-register/README|SVMPX Source Register]].
