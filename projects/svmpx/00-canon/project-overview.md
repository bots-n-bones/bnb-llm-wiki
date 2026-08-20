---
schema: hermes-kb/v2
id: kb-svmpx-project-overview
title: SVMPX Project Overview
project: svmpx
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Канонический обзор назначения SVMPX, операционного процесса, систем данных и provenance Telegram/Notion с явно отмеченными неизвестными.
aliases:
  - Обзор проекта SVMPX
  - Назначение и задачи SVMPX
  - Откуда взяты сведения из Telegram и Notion
tags: [svmpx, overview, operations, pilot]
source_ids:
  - src-gdrive-1GyMW65JutafmAATbqdO-QYFyzYi77-V3
  - src-gdrive-1lt5FdD99OfNsjNLM8yLKEXMpZuRtfQ4ShL8F2B4LS1M
  - src-gdrive-1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4
  - src-gdrive-1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo
  - src-gdrive-1xWgD6_MIpSkKPwVfNb05K6O39JA76BOy
  - src-gdrive-12vfj9ijgI_PDaGHJWUnrjFX05VIKWG_m
  - src-gdrive-12noCwtxbY-_A3AaBKL6t9A4eiX4akFUb
  - src-gdrive-1bmHoD2jBsr15TUt7Ba7MFl5DnBk_QiPg
  - src-gdrive-1LMHdcN8QVQjxhFvVfAw5pHLVgVgj29qB
  - src-gdrive-16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh
created: 2026-08-19
updated: 2026-08-20
---

# SVMPX Project Overview

> Canonical owner-approved overview. Unknown details remain explicitly marked
> and must not be inferred from historical sources.

## Owner-approved purpose and scope

SVMPX is a logistics transportation system that calculates the price and the
quantity of transported goods. Both Electronics and Clothing are active
verticals.

`Purchase Order`, `PO`, `Order`, and `ORD` are names for the same business
entity. `PrePO` / `Preorder` is a deprecated legacy entity and is not part of
the current canonical flow.

## Confirmed facts

SVMPX supports an operational flow from client demand and supplier offers to a
client proposal, a confirmed order, and physical shipments. The reviewed
documentation consistently describes these responsibilities:

- Products is the shared product catalogue. Product records carry identifiers
  and classification data such as EAN, category, brand, model and P/N, plus
  parameters used by later pricing calculations.
- Source Offers stores supplier-specific offer lines rather than master product
  records. The documented structure is source file → SO document → SO line.
- Client Request records what a client asks for before a proposal is assembled.
- Client Proposal combines selected supplier offers, pricing variables and
  client quantities. The proposal is the documented control point for creating
  and later updating an order.
- Purchase Order is the operational order created after quantities are agreed.
  Its progress is aggregated from inbound and outbound Shipments.
- Inbound Shipments represent movement from a supplier to the receiving point;
  Outbound Shipments represent movement toward the client.

The documented working surfaces include structured records and interfaces,
XLSX files for exchange or import, and original files retained on Google Drive.
The owner confirms Airtable as the system of record for structured operational
data and Google Drive as the store for original files. Telegram, n8n, email and
Google Drive are currently used; Make and 1C are not currently used.

## Operational flow supported by the reviewed documentation

```text
Client Request ─┐
                ├─> Client Proposal ─> Purchase Order ─> Shipments IN / OUT
Source Offers ──┘
      ^
      │
   Products
```

The flow above is a conservative synthesis of the `01_documentation` sources
and the owner's terminology decision. `ORD` is represented as Purchase Order;
deprecated `PrePO` is excluded. `Received` is a Shipment status. The meaning of
`DR` remains unconfirmed.

## Current knowledge scope

The legacy master index covers project overview, business processes, system and
interfaces, integrations, file formats, problems, decisions and instructions.
Several entries are explicitly marked as still being collected. The Notion
export map identifies useful source material for system documentation, data
model, bot scenarios, DDP/finance, QA and roadmap, while keeping credentials
outside the curated knowledge base.

This V2 page is therefore a synthesis layer, not evidence that every legacy
section is complete or current.

### Provenance of Telegram and Notion material

Telegram and Notion statements come from registered legacy source records, not
from live runtime inspection. Notion provenance is mapped through the
[[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion export map]].
Telegram inventory and scenarios are registered under the source register and
summarized in [[projects/svmpx/00-canon/bot-scenarios|Bot scenarios]]. Sources
that contained bot secrets remain restricted; secret values were not copied
into the Wiki or search index.

## Conflicting or time-sensitive source statements

1. **DR definition.** The legacy system map includes `DR`, but the owner has not
   confirmed whether it is an entity, document, or state.
2. **Cross-vertical parity.** Electronics and Clothing are both active, but the
   reviewed sources do not prove that every rule and workflow is identical.
3. **User interface boundary.** A roadmap signal proposes moving upload work to
   interfaces and retaining the bot mainly for notifications and statistics.
   Other sources still describe bot-driven operational scenarios.

## Open questions for owner approval

- What exactly is `DR`, and how is it related to a Shipment?
- Which individual n8n workflows implement the confirmed automation layer?
  Brutto is archived; email sends the commercial proposal to an employee.

## Evidence and related drafts

- [[projects/svmpx/04-source-register/sources/supporting/core/project-map|Legacy project map]]
- [[projects/svmpx/04-source-register/sources/master-index|Legacy master index]]
- [[projects/svmpx/04-source-register/sources/system-documentation-map|System documentation map]]
- [[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion export map]]
- [[projects/svmpx/04-source-register/sources/documentation/client-request|Client Request source]]
- [[projects/svmpx/04-source-register/sources/documentation/products-overview|Products source]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-overview|Source Offers source]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-overview|Client Proposal source]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview|Purchase Order source]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-overview|Shipments source]]
- [[projects/svmpx/00-canon/system-documentation|System documentation draft]]
- [[projects/svmpx/00-canon/data-model|Data model draft]]
- [[projects/svmpx/00-canon/ddp-finance-flow|DDP and finance flow draft]]
- [[projects/svmpx/00-canon/bot-scenarios|Bot scenarios draft]]
