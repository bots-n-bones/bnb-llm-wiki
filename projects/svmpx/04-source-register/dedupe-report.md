---
schema: hermes-kb/v2
id: svmpx-drive-dedupe-report-2026-08-19
title: SVMPX Drive Dedupe Report
project: svmpx
type: reference
domain: audit
status: active
canonical: false
owner: codex
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: [svmpx, drive, dedupe, manifest]
---

# SVMPX Drive Dedupe Report

No Drive objects were changed. Every resolution below is pending human approval.

## Coverage

This report is derived from snapshot `svmpx-drive-2026-08-19T151054Z`:

- 246 objects returned (100 folders, 146 files).
- 101 folders opened recursively; no folder reached the requested 1,000-child limit.
- 68 discovered folders returned no children.
- The earlier baseline records 1,466 objects; the 1220-object discrepancy makes this snapshot **partial**.
- Paginated metadata search was unavailable during this run (connector HTTP 403).
- Drive checksums and versions were not exposed. “Probable exact” is not hash proof.

Machine artifacts:

- `audit/manifests/svmpx-drive-manifest-2026-08-19.jsonl`
- `audit/manifests/svmpx-drive-scan-summary-2026-08-19.json`
- `audit/manifests/svmpx-drive-duplicate-groups-2026-08-19.jsonl`

## Rules

1. **Probable exact metadata:** normalized name + MIME type + identical non-null byte size.
2. **Name collision:** normalized name + MIME type, but size may differ.
3. Names are Unicode NFKC-normalized, lowercased, trimmed, whitespace-collapsed, and simple copy suffixes are removed.
4. No file is deletion-safe until content hashes/exports and business ownership are verified.

## Probable exact metadata groups

### svmpx-probable-exact-001: `.ds_store`

- MIME: `application/octet-stream`
- Size: 10244 bytes
- Members: 4
- Decision: **pending human approval**
- Proposed action: compare SHA-256 (or deterministic exports), then select a preferred source; do not delete now.

  - [SVMPX/00_data/.DS_Store](https://drive.google.com/file/d/1GLdvRSURr5_rJvu0AJA-tUJy1usEJ4fp/view?usp=drivesdk) — `1GLdvRSURr5_rJvu0AJA-tUJy1usEJ4fp`
  - [SVMPX/00_data/SVMPX Logistics Export Package 2/.DS_Store](https://drive.google.com/file/d/1LJN1ysEM8bOS2sL801RWwwnMxZjmiU_y/view?usp=drivesdk) — `1LJN1ysEM8bOS2sL801RWwwnMxZjmiU_y`
  - [SVMPX/00_data/ChatExport_2026-06-05/.DS_Store](https://drive.google.com/file/d/1kXxEIFinQe0oCEOu42tShaKEiITVR7-2/view?usp=drivesdk) — `1kXxEIFinQe0oCEOu42tShaKEiITVR7-2`
  - [SVMPX/06_old_notion/SVMPX Logistics Export Package 2/.DS_Store](https://drive.google.com/file/d/1da8O0eK2C2v2gswnH2H8Zk4A1wPIJl7p/view?usp=drivesdk) — `1da8O0eK2C2v2gswnH2H8Zk4A1wPIJl7p`

### svmpx-probable-exact-002: `how_to_export.md`

- MIME: `text/markdown`
- Size: 3026 bytes
- Members: 3
- Decision: **pending human approval**
- Proposed action: compare SHA-256 (or deterministic exports), then select a preferred source; do not delete now.

  - [SVMPX/00_data/SVMPX Logistics Export Package 2/HOW_TO_EXPORT.md](https://drive.google.com/file/d/1einPLAGhcQYi59yGMFJd0hMFSjHojJrS/view?usp=drivesdk) — `1einPLAGhcQYi59yGMFJd0hMFSjHojJrS`
  - [SVMPX/00_data/SVMPX Logistics Export Package/HOW_TO_EXPORT.md](https://drive.google.com/file/d/1exW3xH2RRqoFTw_7Ac8PSbWBmh8gm9Ic/view?usp=drivesdk) — `1exW3xH2RRqoFTw_7Ac8PSbWBmh8gm9Ic`
  - [SVMPX/06_old_notion/SVMPX Logistics Export Package 2/HOW_TO_EXPORT.md](https://drive.google.com/file/d/1utu2aHUdHmsViz6AEHnZCi6fZsIiU0R5/view?usp=drivesdk) — `1utu2aHUdHmsViz6AEHnZCi6fZsIiU0R5`

### svmpx-probable-exact-003: `статусы и ошибки.xlsx`

- MIME: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- Size: 86040 bytes
- Members: 2
- Decision: **pending human approval**
- Proposed action: compare SHA-256 (or deterministic exports), then select a preferred source; do not delete now.

  - [SVMPX/05_backups/Статусы и ошибки.xlsx](https://docs.google.com/spreadsheets/d/1bZTA_sFc0Hc-4zoy9nRm-i3MccWtqt_L/edit?usp=drivesdk&ouid=103073671129499618095&rtpof=true&sd=true) — `1bZTA_sFc0Hc-4zoy9nRm-i3MccWtqt_L`
  - [SVMPX/01_documentation/Статусы и ошибки.xlsx](https://docs.google.com/spreadsheets/d/1kTCv3-YJC2VwJOGYLWHhU3nGDipOIBLq/edit?usp=drivesdk&ouid=103073671129499618095&rtpof=true&sd=true) — `1kTCv3-YJC2VwJOGYLWHhU3nGDipOIBLq`

## Name collisions

These are not deletion candidates without semantic comparison.

### svmpx-name-collision-001: `.ds_store`

- MIME: `application/octet-stream`
- Sizes: 10244, 6148 bytes
- Members: 5
- Decision: **pending human approval**

  - [SVMPX/00_data/.DS_Store](https://drive.google.com/file/d/1GLdvRSURr5_rJvu0AJA-tUJy1usEJ4fp/view?usp=drivesdk) — 10244 bytes — `1GLdvRSURr5_rJvu0AJA-tUJy1usEJ4fp`
  - [SVMPX/00_data/SVMPX Logistics Export Package 2/.DS_Store](https://drive.google.com/file/d/1LJN1ysEM8bOS2sL801RWwwnMxZjmiU_y/view?usp=drivesdk) — 10244 bytes — `1LJN1ysEM8bOS2sL801RWwwnMxZjmiU_y`
  - [SVMPX/00_data/ChatExport_2026-06-05/.DS_Store](https://drive.google.com/file/d/1kXxEIFinQe0oCEOu42tShaKEiITVR7-2/view?usp=drivesdk) — 10244 bytes — `1kXxEIFinQe0oCEOu42tShaKEiITVR7-2`
  - [SVMPX/02_screenshots/Client Proposal/.DS_Store](https://drive.google.com/file/d/1kDXbhetDRAX0Btz6wq1_9mYC1Hn_8cC2/view?usp=drivesdk) — 6148 bytes — `1kDXbhetDRAX0Btz6wq1_9mYC1Hn_8cC2`
  - [SVMPX/06_old_notion/SVMPX Logistics Export Package 2/.DS_Store](https://drive.google.com/file/d/1da8O0eK2C2v2gswnH2H8Zk4A1wPIJl7p/view?usp=drivesdk) — 10244 bytes — `1da8O0eK2C2v2gswnH2H8Zk4A1wPIJl7p`

### svmpx-name-collision-002: `how_to_export.md`

- MIME: `text/markdown`
- Sizes: 3026 bytes
- Members: 3
- Decision: **pending human approval**

  - [SVMPX/00_data/SVMPX Logistics Export Package 2/HOW_TO_EXPORT.md](https://drive.google.com/file/d/1einPLAGhcQYi59yGMFJd0hMFSjHojJrS/view?usp=drivesdk) — 3026 bytes — `1einPLAGhcQYi59yGMFJd0hMFSjHojJrS`
  - [SVMPX/00_data/SVMPX Logistics Export Package/HOW_TO_EXPORT.md](https://drive.google.com/file/d/1exW3xH2RRqoFTw_7Ac8PSbWBmh8gm9Ic/view?usp=drivesdk) — 3026 bytes — `1exW3xH2RRqoFTw_7Ac8PSbWBmh8gm9Ic`
  - [SVMPX/06_old_notion/SVMPX Logistics Export Package 2/HOW_TO_EXPORT.md](https://drive.google.com/file/d/1utu2aHUdHmsViz6AEHnZCi6fZsIiU0R5/view?usp=drivesdk) — 3026 bytes — `1utu2aHUdHmsViz6AEHnZCi6fZsIiU0R5`

### svmpx-name-collision-003: `messages.html`

- MIME: `text/html`
- Sizes: 441933, 1126964 bytes
- Members: 2
- Decision: **pending human approval**

  - [SVMPX/00_data/ChatExport_2026-06-05/messages.html](https://drive.google.com/file/d/1Gl99b-owC_SVB6tyFUAlWeHV5UvcFduN/view?usp=drivesdk) — 441933 bytes — `1Gl99b-owC_SVB6tyFUAlWeHV5UvcFduN`
  - [SVMPX/00_data/ChatExport_2026-06-05 (1)/messages.html](https://drive.google.com/file/d/1pbdB932IHmBrv7pmVFJCLKcLEOegDNvJ/view?usp=drivesdk) — 1126964 bytes — `1pbdB932IHmBrv7pmVFJCLKcLEOegDNvJ`

### svmpx-name-collision-004: `readme.md`

- MIME: `text/markdown`
- Sizes: 2536, 1069, 622, 612, 551 bytes
- Members: 5
- Decision: **pending human approval**

  - [SVMPX/00_data/SVMPX Logistics Drive Structure/README.md](https://drive.google.com/file/d/1CJ50nO4H4hQuFsy7t8-JUp5mAUbrkPSP/view?usp=drivesdk) — 2536 bytes — `1CJ50nO4H4hQuFsy7t8-JUp5mAUbrkPSP`
  - [SVMPX/00_data/SVMPX Logistics Knowledge Base/README.md](https://drive.google.com/file/d/17LxQ52ohlESLuFz55p6oqbRZ7dW6QDmh/view?usp=drivesdk) — 1069 bytes — `17LxQ52ohlESLuFz55p6oqbRZ7dW6QDmh`
  - [SVMPX/00_data/SVMPX Logistics Drive Structure/02 - Source Offers/README.md](https://drive.google.com/file/d/1QmdtHsUDb5xaAOXZCQVKHLcDDwGRPkep/view?usp=drivesdk) — 622 bytes — `1QmdtHsUDb5xaAOXZCQVKHLcDDwGRPkep`
  - [SVMPX/00_data/SVMPX Logistics Drive Structure/07 - Shipments/README.md](https://drive.google.com/file/d/1oklphulJPuqdRRuD2W3ZhC07u6YU--tK/view?usp=drivesdk) — 612 bytes — `1oklphulJPuqdRRuD2W3ZhC07u6YU--tK`
  - [SVMPX/00_data/SVMPX Logistics Drive Structure/99 - Source Archive/README.md](https://drive.google.com/file/d/1cHyBxFhrd0hJBdqliF5Lwi-WsxecnT3I/view?usp=drivesdk) — 551 bytes — `1cHyBxFhrd0hJBdqliF5Lwi-WsxecnT3I`

### svmpx-name-collision-005: `статусы и ошибки.xlsx`

- MIME: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- Sizes: 86040 bytes
- Members: 2
- Decision: **pending human approval**

  - [SVMPX/05_backups/Статусы и ошибки.xlsx](https://docs.google.com/spreadsheets/d/1bZTA_sFc0Hc-4zoy9nRm-i3MccWtqt_L/edit?usp=drivesdk&ouid=103073671129499618095&rtpof=true&sd=true) — 86040 bytes — `1bZTA_sFc0Hc-4zoy9nRm-i3MccWtqt_L`
  - [SVMPX/01_documentation/Статусы и ошибки.xlsx](https://docs.google.com/spreadsheets/d/1kTCv3-YJC2VwJOGYLWHhU3nGDipOIBLq/edit?usp=drivesdk&ouid=103073671129499618095&rtpof=true&sd=true) — 86040 bytes — `1kTCv3-YJC2VwJOGYLWHhU3nGDipOIBLq`

## Decision queue

| Priority | Group | Required evidence | Proposed owner decision |
|---|---|---|---|
| P1 | `svmpx-probable-exact-001` | SHA-256/export hash + open/read comparison | choose preferred source or retain all |
| P1 | `svmpx-probable-exact-002` | SHA-256/export hash + open/read comparison | choose preferred source or retain all |
| P1 | `svmpx-probable-exact-003` | SHA-256/export hash + open/read comparison | choose preferred source or retain all |
| P2 | `svmpx-name-collision-003` | semantic comparison and lifecycle context | classify as distinct/version/duplicate |
| P2 | `svmpx-name-collision-004` | semantic comparison and lifecycle context | classify as distinct/version/duplicate |

## Gate

Do not move, rename, archive, or delete anything until:

- a paginated full manifest is available;
- hashes or deterministic export hashes are recorded;
- references to each candidate are checked;
- Ilya approves `preferred_source_id` and the action;
- a recoverable archive/rollback path is documented.

