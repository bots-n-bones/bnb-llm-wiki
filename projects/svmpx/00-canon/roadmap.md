---
schema: hermes-kb/v2
id: kb-svmpx-roadmap
title: SVMPX Roadmap
project: svmpx
type: canon
domain: planning
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: "Черновой план: какие доработки запланированы, какие решения устарели и как проверить исторический roadmap SVMPX Q4 2025."
aliases:
  - План доработок SVMPX
  - Запланированные и устаревшие решения
tags: [svmpx, roadmap, planning, priorities]
source_ids:
  - src-gdrive-1EA9B6HfFkgAsHyZc5o4XpOR8giXM7wPPw04AJaoHuUA
  - src-gdrive-1lt5FdD99OfNsjNLM8yLKEXMpZuRtfQ4ShL8F2B4LS1M
  - src-gdrive-1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo
related:
  - projects/svmpx/00-canon/project-overview
  - projects/svmpx/00-canon/system-documentation
  - projects/svmpx/00-canon/data-model
  - projects/svmpx/00-canon/bot-scenarios
  - projects/svmpx/00-canon/ddp-finance-flow
  - projects/svmpx/00-canon/qa-protocol
created: 2026-08-19
updated: 2026-08-20
---

# SVMPX Roadmap

This page is the canonical interpretation of the available planning evidence.
The dated Q4 2025 roadmap below is preserved as historical evidence; its items
are not current commitments, approved dates, or approved priorities in 2026.

During owner review on 2026-08-20, the current relevance of the Q4 2025 plan
and the location of any replacement roadmap could not be confirmed. Hermes
must therefore treat every Q4 2025 item as historical evidence, not as a
current commitment, deadline, or priority.

## Confirmed current boundaries

Airtable remains the primary operational interface and system of record;
original and generated files are stored on Google Drive. Brutto is archived and
its functions are disabled. Electronics and Clothing require functional parity
except that an Electronics PO may cover multiple suppliers while a Clothing PO
always has exactly one supplier.

## Confirmed from sources

### Historical Q4 2025 plan

The [SVMPX Electronics Q4 2025 Roadmap](https://docs.google.com/document/d/1EA9B6HfFkgAsHyZc5o4XpOR8giXM7wPPw04AJaoHuUA/edit)
records these work blocks and weights:

| Historical block | Stated purpose | Source weight |
|---|---|---:|
| Client comments | Move client corrections into interfaces and separate them from system notes | 15% |
| Pipeline finance | Unify the finance flow across `SO → CP → ORD → SHP → Received → DR` | 25% |
| Target-price fitting | Calculate conditions against the client's target price and highlight deviations | 10% |
| Client needs | Import requests, check them against Products/Offers, and prepare a draft CP/PrePO | 10% |
| Personalized interfaces | Provide role-oriented views for managers, logistics, and analysts | 10% |
| Clothing migration | Transfer tables, links, formulas, and interfaces from Electronics | 15% |
| Brutto bot | Shift the bot toward notifications and statistics through n8n | 10% |
| Logistics chains 2.0 | Compare current, proposed, and optimal scenarios in `Logistic Scenarios` | +20% |

The source uses `+20%` for Logistics chains 2.0, so the values must not be
normalized or treated as a capacity allocation without clarification.

The same source requests client input on financial amounts, the target-price
process, client-needs process, interface preferences, and logistics-chain data.
It also records a proposed target role for the Brutto bot: notifications,
statistics, and reports, while primary work happens in Airtable interfaces.

Registered provenance:
[[projects/svmpx/04-source-register/sources/supporting/quality/electronics-q4-2025-roadmap|Electronics Q4 2025 roadmap source record]].

### Documentation state

The [[projects/svmpx/04-source-register/sources/master-index|legacy master index]]
provides a nine-part navigation taxonomy but does not prove that each linked
page is current. The
[[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion export map]]
identifies roadmap, QA protocol, system documentation, data model, bot scenarios,
and DDP/finance flow as proposed canonical outputs. The
[[projects/svmpx/04-source-register/sources/documentation-index|operational documentation index]]
registers 21 source documents that still require implementation verification.

## Proposed current sequence

No dates or completion percentages are proposed until the unresolved current
state is confirmed.

### Phase 0 — Establish the current baseline

- Approve terminology and scope in
  [[projects/svmpx/00-canon/project-overview|Project overview]].
- Compare source claims against the live implementation and identify which Q4
  2025 items are done, partial, retired, or not started.
- Assign an owner and evidence link to every retained roadmap item.
- Resolve contradictions before promoting any draft to canonical status.

**Exit condition:** a human-approved current-state matrix exists for every
historical roadmap block.

### Phase 1 — Stabilize core operational flows

- Confirm the implemented flows in
  [[projects/svmpx/00-canon/system-documentation|System documentation]].
- Approve entities and relationships in
  [[projects/svmpx/00-canon/data-model|Data model]].
- Execute an evidenced baseline using
  [[projects/svmpx/00-canon/qa-protocol|QA protocol]].

**Exit condition:** the supported product, offer, proposal, order, and shipment
paths are documented and have reviewed QA evidence.

### Phase 2 — Resolve finance and pricing behavior

- Approve the chain, formulas, responsibilities, and fixtures in
  [[projects/svmpx/00-canon/ddp-finance-flow|DDP and finance flow]].
- Decide how target-price fitting relates to DDP and other financial values.
- Obtain the missing client definitions for displayed and tracked amounts.

**Exit condition:** the finance and target-price rules are unambiguous and
testable with approved fixtures.

### Phase 3 — Confirm interfaces and client-needs workflow

- Decide which roles require dedicated views and which comments are client or
  system-owned.
- Define the input, matching, and draft-output behavior for Client Needs.
- Verify that proposed interface work reflects current user workflows.

**Exit condition:** approved user flows and acceptance criteria exist for the
retained interface and Client Needs scope.

### Phase 4 — Decide domain parity and migration scope

- Compare Electronics and Clothes behavior using the approved QA matrix.
- Classify each feature as shared, domain-specific, migrated, or retired.
- Plan only the verified gaps; do not repeat completed migration work.

**Exit condition:** a reviewed gap list replaces the broad historical
"Clothing migration" item.

### Phase 5 — Confirm logistics evolution

- Preserve the archived Brutto scenarios as historical evidence; do not plan
  reactivation without a new owner decision and security review.
- Define current, proposed, and optimal logistics scenarios and their comparison
  criteria.
- Sequence implementation only after owners and source data are available.

**Exit condition:** logistics 2.0 requirements have explicit human approval and
testable acceptance criteria.

## Unresolved before approval

- What is the present implementation status of every Q4 2025 block?
- Is the historical priority weighting still meaningful, and what does `+20%`
  represent?
- Have the five requested client inputs been received, and where is their
  authoritative source?
- Which roadmap items are product commitments versus research or options?
- Who owns each retained item, what are its dependencies, and what dates are
  approved?
- Which acceptance evidence is required before an item can be marked complete?

Until a replacement roadmap is explicitly approved by the owner, this page
must not be used as a delivery commitment.
