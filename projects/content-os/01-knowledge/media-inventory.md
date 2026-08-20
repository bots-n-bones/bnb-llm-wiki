---
schema: hermes-kb/v2
id: kb-content-os-media-inventory
title: "Content OS media inventory"
project: content-os
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [media, inventory]
source_ids:
  - kb-content-os-source-media-metadata-snapshot
derived:
  method: local-recursive-media-manifest-v2
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Content OS media inventory

After policy exclusions, the local tree contains 993 media files totaling
1,557,247,902 bytes: 532 PNG, 251 JPG, 78 JPEG, 115 MP4, 15 MOV, and 2 MP3.

Only aggregate filesystem metadata was retained. Payloads, previews, embedded
metadata, and individual filenames are outside this draft. `node_modules`,
`.git`, `dist`, `build`, `.cache`, and `__pycache__` are excluded.
