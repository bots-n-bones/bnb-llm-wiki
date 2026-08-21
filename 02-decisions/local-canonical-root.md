---
schema: hermes-kb/v2
id: decision-bnb-local-canonical-root
title: Local canonical file root
type: decision
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: "`BnB Project — Canonical` is the working local original-file root; the three downloaded fragments are immutable Legacy evidence."
created: 2026-08-21
updated: 2026-08-21
tags: [decision, local-source, canonical-root, legacy]
---

# Local canonical file root

Ilya approved `/Users/ilya/Downloads/BnB Project — Canonical` as the local
working root on 2026-08-21.

The downloaded `bots-n-bones`, `bots-n-bones 2` and `bots-n-bones 3` fragments
remain unchanged as read-only Legacy evidence. They are not working roots and
must not be deleted, renamed, reorganized or used as a silent fallback for
Hermes attachment retrieval.

The canonical root is a verified union of 3,057 preferred supporting files.
Exact duplicates, archives, technical files, restricted artifacts and
macro-capable workbooks were excluded. The materialization receipt and SHA-256
inventory are retained under `audit/local/`.

If a canonical copy is absent or has a different checksum, attachment lookup
must fail closed and request a manifest refresh.

See [[audit/local/bnb-local-cleanup-proposal]] and
[[projects/svmpx/01-knowledge/original-file-catalog]].
