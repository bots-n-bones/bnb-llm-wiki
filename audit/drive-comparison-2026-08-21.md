---
schema: hermes-kb/v2
id: kb-drive-comparison-2026-08-21
title: Read-only Drive comparison — primary and incomplete BnB roots
type: index
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-21
updated: 2026-08-21
tags: [audit, google-drive, provenance, deduplication]
---

# Read-only Drive comparison — 2026-08-21

This audit compared metadata only. It did not download, move, rename, share,
or delete any Google Drive object.

## Scope

- Primary source root: `1k5s_Gn_oCydPx4AP4IpCpvCl0-c6N15j`.
- Separate incomplete reference root: `1z0FSy1pdrmAK5paKqAguxOIBPypwFiNn`.
- Existing local audit snapshot: `audit/local/bnb-local-manifest.jsonl`.

## Result

The primary Drive root contains 11,852 files (6,945,082,631 bytes). The
existing local snapshot contains 11,854 files (6,948,850,676 bytes), so it is
already a near-complete local copy of the primary source; a wholesale download
would be unnecessary.

The incomplete reference root contains 4,383 files (5,014,665,093 bytes).
Of these, 4,337 have the same normalized filename and size as files in the
primary root. The remaining 46 are native Google Docs or Sheets variants,
often repeated several times, and are retained only as untrusted review
candidates. They are not imported, promoted, or used to alter canon.

The combined folder traversal inspected 19,656 items in 3,427 folders. No
folder response was truncated and no listing error occurred.

## Current local availability

At the time of this audit, the historical local artifact directories
`BnB Project` and `BnB Project — Canonical` were no longer present at their
recorded paths. The manifest, source records, curated Markdown, and safe local
search index remain available. Do not claim to have re-extracted text from an
original unless the artifact is later restored or retrieved from Drive.

## Decision

Do not re-download the primary root at this stage. Keep the incomplete root
separate from canonical ingestion. Any future retrieval must be limited to a
specific missing source after provenance, duplicate, secret, and lifecycle
checks.
