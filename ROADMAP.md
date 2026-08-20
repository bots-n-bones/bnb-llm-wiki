---
schema: hermes-kb/v2
id: kb-v2-roadmap
title: KB V2 Implementation Roadmap
type: index
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-19
updated: 2026-08-20
tags: [roadmap, svmpx, implementation]
---

# KB V2 Implementation Roadmap

## Gate 0 — source baseline

- [x] Identify and compare all verified SVMPX roots.
- [x] Select the shared root as immutable source candidate.
- [x] Record verified depth-4 audit statistics and duplicate indicators.
- [x] Store a reproducible partial connector snapshot and its coverage report.
- [ ] Produce complete recursive JSONL and CSV manifests.
- [ ] Hash the manifest and commit its checksum.
- [ ] Confirm all folders discovered at the audit boundary are expanded.

## Gate 1 — source classification

- [x] Register the legacy source register, master index, system map, and Notion
  export map.
- [x] Register 21/21 knowledge-bearing Markdown files from `01_documentation`.
- [ ] Classify Notion and Telegram exports as evidence, backup, restricted, or
  out of scope.
- [x] Produce a partial-evidence dedupe report with all decisions pending human
  approval.

## Gate 2 — canonical drafts

- [x] Project overview draft.
- [x] System documentation draft.
- [x] Data model draft.
- [x] Bot scenarios draft.
- [x] DDP and finance flow draft.
- [x] QA protocol draft.
- [x] Roadmap draft.

All drafts remain non-canonical until human review.

## Gate 3 — Hermes MVP

- [x] Refactor the knowledge backend without changing existing API behavior.
- [x] Add stable IDs, aliases, source metadata, relationship parsing, and
  collision-safe UI navigation.
- [x] Add ranked Unicode lexical search for natural Russian questions and
  targeted tests.
- [x] Add SQLite manifest and FTS5 search with Russian-language tests.
- [ ] Add metadata-only readonly Drive ingestion for the allowlisted SVMPX root.
- [x] Add asynchronous persisted synchronization runs for the local-first
  provider; Google Drive remains deferred.
- [x] Connect the local private-repository checkout to the local pilot
  environment.

## Gate 4 — acceptance

- [x] Validate all metadata, source IDs, provenance fields, JSONL, and links.
- [x] Certify all 60 pre-approval golden queries against the materialized,
  authority-ranked SQLite index across the six projects and shared knowledge.
  Unapproved SVMPX canon targets intentionally resolve to their safe active
  source pages; post-approval canonical routing remains a separate gate.
- [x] Confirm the legacy Drive roots were not moved, renamed, overwritten, or
  deleted during the pilot.
- [x] Obtain owner approval for the seven SVMPX canonical pages.
- [x] Re-run the 60-query certificate against approved canonical targets.
- [ ] Merge the pilot branch to `main` and tag `svmpx-pilot-v1`.

See [[00-governance/architecture|KB V2 Architecture]] and
[[audit/drive-baseline-summary-2026-08-19|SVMPX Drive Baseline Summary]].
