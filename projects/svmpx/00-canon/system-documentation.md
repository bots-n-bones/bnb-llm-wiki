---
schema: hermes-kb/v2
id: kb-svmpx-system-documentation
title: SVMPX System Documentation
project: svmpx
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Каноническая архитектура и компоненты SVMPX, путь заказа, Airtable, n8n, Google Drive, email, импорт и ImportLogs.
aliases:
  - Архитектура SVMPX
  - Компоненты системы SVMPX
  - Из каких компонентов состоит архитектура SVMPX
  - Импорт и ImportLogs
  - Путь заказа SO—DR
tags: [svmpx, system, architecture, operations]
source_ids:
  - src-gdrive-148YsufxFgmJ85E4-3IjEYEpwJLFRUa1FofcG8Qxw3Ds
  - src-gdrive-1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4
  - src-gdrive-1lt5FdD99OfNsjNLM8yLKEXMpZuRtfQ4ShL8F2B4LS1M
  - src-gdrive-1o7akXBWg7xOpdi60VvaSIXm64EHLjKFUR77gg-MnTJo
  - src-gdrive-12vfj9ijgI_PDaGHJWUnrjFX05VIKWG_m
  - src-gdrive-12noCwtxbY-_A3AaBKL6t9A4eiX4akFUb
  - src-gdrive-1NbUlBCwIyXCI8U-hrT0BF6yZvEMIJ9a7
  - src-gdrive-1wL-K24aO0CxQgRKvu7Upn4OpvMYcvNFK
  - src-gdrive-1z_6teccMfe5mKw9tHdjU7Hl266-VyhbD
  - src-gdrive-1lDvVIA19MTx1WRzt2rRyJTTq_r0ofODJ
  - src-gdrive-1OR6h15u1TEFm7ijB1IbsjzEzhRrVao51
created: 2026-08-19
updated: 2026-08-20
---

# SVMPX System Documentation

> Canonical architecture and behavior map approved by the owner. Statements
> labelled “candidate” remain legacy or planning claims and are not promoted to
> current production facts.

## Confirmed operational behavior

### Catalogue and offer intake

Products is the master catalogue used by downstream offer and pricing flows.
Source Offers stores supplier-specific offer lines connected to Products. The
reviewed interface documentation exposes offer price, quantity, validity,
supplier context and a DDP calculation area. Broken product links and DDP
calculation failures are represented as problem states.

### Proposal and order control

A Client Proposal is created from selected Source Offer lines. A proposal moves
through documented stages including Draft, Sent to client, Agreement and PO
Created. Client-requested and supplier-confirmed quantities can differ. The
documented control rule is that order composition changes are applied through
the Client Proposal and then propagated to the order; the PO is not treated as
the primary manual editing surface.

### Logistics execution

Purchase Orders aggregate ordered products and execution data. Inbound and
Outbound Shipment records capture planned and actual movement. Documented
Shipment stages are Draft, Planned, In Transit, Received, and Closed or Closed
with warnings. Shipment quantities and states feed progress and warnings back
to the Purchase Order.

Inbound requires supplier selection and planned departure/arrival dates. The
reviewed Outbound guide requires a linked PO, direction, transport mode, dates,
quantities, and a mandatory Supplier field.

The owner has not defined one canonical date format; both legacy formats remain
non-canonical. File names may be arbitrary and are not required to follow a
strict naming mask.

## Owner-confirmed current architecture

The owner confirms the following current boundaries:

| Component | Current status and responsibility |
|---|---|
| Airtable | Active system of record for structured operational entities |
| Telegram bot | Active; exact live commands and write flows still require inventory |
| n8n | Active; owns the system's automation logic |
| Google Drive | Active store for original files |
| Email | Active; sends the commercial proposal to an employee's email |
| Make | Not currently used |
| 1C | Not currently used |

No credentials, endpoints or tokens belong in this page. Their existence may be
referenced, but secret material remains outside KB V2.

## Candidate import contract

The system map specifies these rules as targets requiring implementation
verification:

- primary exchange format is XLSX;
- an import reports `accepted → validating → result`;
- result counts include `added`, `updated` and `skipped`;
- candidate product deduplication keys include EAN, P/N, Model and SKU;
- ImportLogs should capture user, action, filename, result counts, errors,
  timestamps and a correlation ID.

These statements describe a desired or previously documented contract. They do
not prove that every live importer currently implements it.

## System-of-record boundary

The owner confirms Airtable as the system of record for Product, Supplier,
Client, Source Offer, Client Proposal, Purchase Order and Shipment data. Google
Drive stores the original files. `Received` is a Shipment status. Detailed
conflict-resolution rules remain to be documented. Original files are moved to
archive storage on Google Drive instead of being physically deleted. A Client
Proposal file is sent to Drive while its Airtable record remains in place; see
[[projects/svmpx/00-canon/data-model|Data model draft]].

## Conflicting or incomplete source statements

1. **Date format.** Sources contain both `DD.MM.YYYY` and `YYYY-MM-DD`; the
   owner confirms that a single standard is not currently defined.
2. **Bot boundary.** Sources describe Telegram uploads, but Brutto has now been
   confirmed as an archived component with all operational functions disabled.
3. **Environment and operations.** Dev/Stage/Prod, backups, monitoring, SLA and
   rollback appear in the target outline but are not evidenced as implemented.

## Open verification checklist

- Export or inspect the current Airtable schema and compare it to this draft.
- Inventory active Telegram commands and write permissions.
- Inventory the individual n8n workflows behind the confirmed automation layer.
- Trace one real Source Offer through CP, PO and both Shipment directions.
- Verify import idempotency, logs and duplicate handling with a safe test file.
- Decide whether a canonical date standard is needed; arbitrary file names are
  currently allowed.
- Define backup, recovery, monitoring and change-management ownership.

## Evidence and related drafts

- [[projects/svmpx/04-source-register/sources/supporting/core/system-002-1|System 002.1 outline]]
- [[projects/svmpx/04-source-register/sources/system-documentation-map|System documentation map]]
- [[projects/svmpx/04-source-register/sources/master-index|Legacy master index]]
- [[projects/svmpx/04-source-register/sources/notion-full-export-map|Notion export map]]
- [[projects/svmpx/04-source-register/sources/documentation/products-overview|Products overview]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-overview|Source Offers overview]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow|Client Proposal workflow]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-orders-interface|Purchase Orders interface]]
- [[projects/svmpx/04-source-register/sources/documentation/shipment-in-create|Inbound Shipment guide]]
- [[projects/svmpx/04-source-register/sources/documentation/shipment-out-create|Outbound Shipment guide]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-status-errors|Shipment states and errors]]
- [[projects/svmpx/00-canon/project-overview|Project overview draft]]
- [[projects/svmpx/00-canon/data-model|Data model draft]]
- [[projects/svmpx/00-canon/bot-scenarios|Bot scenarios draft]]
- [[projects/svmpx/00-canon/qa-protocol|QA protocol draft]]
