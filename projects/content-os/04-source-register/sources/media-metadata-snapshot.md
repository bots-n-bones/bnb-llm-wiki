---
schema: hermes-kb/v2
id: kb-content-os-source-media-metadata-snapshot
title: "Content OS media metadata snapshot"
project: content-os
type: source-record
status: draft
canonical: false
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [local-source, media-metadata, portfolio-audit]
source:
  kind: local-directory-metadata-snapshot
  drive_file_id: "local:e4c5346ef4ecf57f6ec0a897b0f69fc530f2dfd9b8cbd7c26210333bfa12afb6"
  url: "urn:sha256:e4c5346ef4ecf57f6ec0a897b0f69fc530f2dfd9b8cbd7c26210333bfa12afb6"
  parent_folder_id: "local-parent:content-os"
  original_path: "/Users/ilya/Downloads/BnB Project Consolidated/bots-n-bones/01 - projects/content-os"
  original_title: "content-os recursive media inventory"
  mime_type: "application/x-directory-metadata"
  modified_time: "2026-05-18T20:55:40Z"
  checksum: "sha256:e4c5346ef4ecf57f6ec0a897b0f69fc530f2dfd9b8cbd7c26210333bfa12afb6"
  revision_id: "recursive-media-manifest-v2;files:993;bytes:1557247902"
---

# Content OS media metadata snapshot

Recursive aggregate derived from a deterministic in-memory manifest. Each media
file contributes `relative POSIX path<TAB>byte size<TAB>mtime_ns`; UTF-8 lines
are sorted by Unicode code point, joined with LF, and terminated with LF before
SHA-256 is calculated. `node_modules`, `.git`, `dist`, `build`, `.cache`, and
`__pycache__` are excluded. No media payload, embedded metadata, or filename
list was copied into the Wiki.
