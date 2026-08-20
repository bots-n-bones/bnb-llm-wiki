---
schema: hermes-kb/v2
id: audit-git-baseline-2026-08-19
title: Git Baseline Before KB V2 Pilot
type: reference
status: active
canonical: false
owner: codex
confidentiality: internal
created: 2026-08-19
updated: 2026-08-19
tags: [audit, git, rollback]
---

# Git Baseline Before KB V2 Pilot

- Repository: `bots-n-bones/hermes-workspace`
- Branch: `github-main`
- HEAD: `4da29447312e82787e4084c609f7b563e9c7646f`
- Existing status before KB V2 files: 1,041 added, 6 modified, 123,000
  deleted, 136 renamed, 0 untracked entries.

The working tree was already heavily modified before this pilot. No protective
branch or commit was created because that would mix unrelated pre-existing work
with KB V2. The files under `knowledge-v2/` are intentionally isolated until the
repository baseline is reconciled.
