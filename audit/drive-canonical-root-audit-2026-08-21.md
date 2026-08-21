---
schema: hermes-kb/v2
id: kb-drive-canonical-root-audit-2026-08-21
title: Complete canonical Drive root metadata audit — 2026-08-21
type: index
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-21
updated: 2026-08-21
tags: [audit, google-drive, manifest, checksum, provenance]
---

# Complete canonical Drive root metadata audit — 2026-08-21

The production Hermes server completed a read-only metadata inventory of the
canonical `bots-n-bones` Drive root
`1VfCO8UnD0Qq4D6k-f-HTk7ELgy9j0XOg`. No file body was downloaded during this
audit and no Drive object was changed.

## Receipt

- Snapshot: `drive-inbox-20260821T140128Z`.
- Objects below the root: 10,505.
- Files: 8,505.
- Folders: 2,000.
- Listing or processing errors: 0.
- Complete JSONL manifest: 10,505 records, 8,426,035 bytes.
- Complete CSV manifest: 10,505 data rows, 5,021,175 bytes.
- JSONL snapshot SHA-256:
  `78cdab6161b74708086075fc96e3f6421de5a197a1de7c55c94a50e75f84aed6`.
- CSV snapshot SHA-256:
  `b6350fa8796102fd9f9b3ca5ebfd5f77cb4cedc863f650361af9ecc16d2f582a`.
- Stable inventory SHA-256 (timestamps excluded):
  `83269308f28834b0e252d055f2781e28fb522a813ecb0c5a9860581f61f460de`.

The complete manifests remain in private Hermes state at
`/opt/data/knowledge-drive-audit`. They are intentionally not committed to the
public Wiki because paths and filenames may disclose internal information. This
checksum receipt is the public reproducibility boundary.

## Coverage method

The readonly Drive API was paginated across the account-visible metadata set.
The audit then reconstructed the descendant graph from parent IDs and expanded
every folder reachable from the allowlisted root. This avoids connector
depth/1,000-child limits while excluding objects outside the root.

The same metadata-only audit is scheduled daily. Inbox extraction remains a
separate differential process and still requires owner approval before any
staged material can be published.
