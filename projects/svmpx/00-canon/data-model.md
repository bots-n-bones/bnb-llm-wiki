---
schema: hermes-kb/v2
id: kb-svmpx-data-model
title: SVMPX Data Model
project: svmpx
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: "Каноническая модель данных SVMPX: основные сущности и связи, PO/ORD, устаревший PrePO и дедупликация Product исключительно по EAN."
aliases:
  - Модель данных SVMPX
  - Сущности и связи
  - Какие основные сущности и связи есть в модели данных
  - PO ORD и PrePO
  - Чем отличаются PO ORD и PrePO
  - Дедупликация товаров
  - Поля дедупликации товаров
  - По каким полям выполняется дедупликация товаров
tags: [svmpx, data-model, entities, relationships]
source_ids:
  - src-gdrive-148YsufxFgmJ85E4-3IjEYEpwJLFRUa1FofcG8Qxw3Ds
  - src-gdrive-1BdMDQU1MzZ667ypuaQOMLBzlr4e4zp8yp79K-6LY9I4
  - src-gdrive-12vfj9ijgI_PDaGHJWUnrjFX05VIKWG_m
  - src-gdrive-1Zp57yQSa9pPbzY4AjWYsVdhHqT_3hzte
  - src-gdrive-12noCwtxbY-_A3AaBKL6t9A4eiX4akFUb
  - src-gdrive-1kQpu9whZthTykb9oltDnWgVjmnK17FkH
  - src-gdrive-1xWgD6_MIpSkKPwVfNb05K6O39JA76BOy
  - src-gdrive-1bmHoD2jBsr15TUt7Ba7MFl5DnBk_QiPg
  - src-gdrive-1NbUlBCwIyXCI8U-hrT0BF6yZvEMIJ9a7
  - src-gdrive-1LMHdcN8QVQjxhFvVfAw5pHLVgVgj29qB
  - src-gdrive-1wL-K24aO0CxQgRKvu7Upn4OpvMYcvNFK
  - src-gdrive-16YfHH_Ji4QRNue9YpVA70WNFWdIu-Hoh
created: 2026-08-19
updated: 2026-08-20
---

# SVMPX Data Model

> Canonical business model approved by the owner. It is not a field-level
> Airtable schema and does not assert undocumented cardinalities.

## Owner-approved terminology

`Purchase Order`, `PO`, `Order`, and `ORD` denote the same entity. `PrePO` /
`Preorder` is deprecated and excluded from the current model. `Received` is a
Shipment status, not a separate entity. Both Electronics and Clothing are
active verticals. Airtable is the system of record for structured entities;
Google Drive stores original files.

Product uniqueness is determined exclusively by `EAN`; `P/N`, `Model`, and
`SKU` are not fallback uniqueness keys. A Client Proposal belongs to exactly
one client, one currency, and one legal entity. An Electronics PO may cover
multiple suppliers, while a Clothing PO always belongs to exactly one supplier.
`Same Product` links duplicate Product cards. Partial receipts, shortages, and
returns are represented inside the related Shipment rather than as separate
entities. `Received quantity` cannot exceed `Shipped quantity`; exceeding it is
a validation error. Price and the manually entered exchange rate are
snapshotted when the Client Proposal is created. Original files are not
physically deleted: they are moved to archive storage on Google Drive.
The generated Client Proposal file is sent to Google Drive, while the Client
Proposal record remains in Airtable.

The confirmed Airtable table names are `Products`, `Source Offers`,
`Client Requests`, `Client Proposals`, `Purchase Orders`, and `Shipments`. The
quantity chain is `requested → offering → proposal → placed → shipped →
received`; every following quantity must not exceed the previous quantity.
Integrations use the standard Airtable Record ID form `rec…`. Operational
records normally remain in Airtable rather than being physically deleted.

## Confirmed domain concepts

| Entity or concept | Source-backed responsibility | Documented fields or signals |
|---|---|---|
| Product | Master catalogue record reused downstream | EAN as the unique key; Department, Category, Brand, Model, P/N, Color, Notes; category-derived Tariff and Pcs per Pallet; Same Product links duplicate cards |
| Supplier | Supplier context for offers and inbound logistics | Region, country, currency, VAT; exact master fields require schema verification |
| Client | Customer linked to requests, proposals, orders and outbound work | Identity is referenced, but master fields are not documented in the reviewed set |
| Source Offer document (SO) | One ingested supplier-offer document/file context | Supplier/date/file identity and link to the original SO file |
| Source Offer line (SOL) | One supplier offer for one product in one file | Product link, EXW price, offered quantity, validity, offer type, MOQ, ETA and DDP outputs |
| Client Request (CR) | Initial expression of client demand | Client, requested products, quantities, desired dates, comments, priority and optional target prices |
| Client Proposal (CP) | Commercial selection and calculation workspace | Client, manager, suppliers, selected offer lines, quantities, finance variables, file-generation and workflow state |
| Purchase Order (PO) | Confirmed operational order created from CP | Products/lines, ordered and placed quantities, money metrics, aggregated Shipment state |
| PO Line | Product-level operational detail within an order | Product, supplier and status context are documented; exact keys require schema inspection |
| Shipment | Physical movement linked to a PO | Direction, planned/actual dates, quantities, state, warnings, partial receipts, shortages and returns |
| ImportLog | Candidate audit record for ingestion | User, action, filename, result counts, errors, timestamps and correlation ID |

## Source-backed relationships

```text
Product <── Source Offer Line ──> Supplier
                  │
Source Offer Document ──────────┘
                  │ selected into
                  v
Client Request ─> Client Proposal ─> Purchase Order ─> PO Line
                         │                    │
                       Client                 └─> Shipment IN / OUT
```

The diagram expresses only relationships described by the reviewed sources. It
does not specify database cardinalities or ownership/cascade rules.

### Product and Source Offer

Products is the reusable catalogue. A Source Offer line connects one supplier
offer to a Product and contains transaction-specific price, quantity, validity
and DDP data. Offer history is aggregated back into Product analytics, including
EXW price ranges, offer count and supplier lists.

The source documents describe file → SO document → SO lines. Whether one file
can create multiple SO documents, and the precise uniqueness key for SOL, must
be verified from the current schema and importer.

### Client Request and Client Proposal

Client Request represents desired products and quantities before supplier
selection. Client Proposal is assembled from Source Offer lines. Products may
have multiple supplier offers inside a proposal, while the documented user flow
selects one offer for the client-facing result.

The relationship between CR and CP is conceptually documented, but the reviewed
sources do not prove that every CP must originate from exactly one CR.

### Client Proposal and Purchase Order

After client and supplier quantities are recorded, a CP creates a PO. Sources
say later product/order changes are initiated in CP and propagated to PO. This
implies CP is the control surface, but does not establish whether historical
proposal snapshots or revisions are retained.

### Purchase Order and Shipments

A PO aggregates product lines and execution progress from Inbound and Outbound
Shipments. Inbound handles supplier-to-receiving movement; Outbound handles
movement toward the client. Shipment quantities and statuses contribute to PO
metrics and status.

## Candidate identifiers and validation

- Product matching and deduplication use `EAN` as the only uniqueness key.
- CP identifiers are described in legacy material as `CP#####`.
- Shipment documentation shows a human-readable identifier combining a prefix,
  a PO reference, direction and sequence, but its exact canonical mask is not
  approved.
- SO identifiers visibly combine supplier, date and source filename in the
  reviewed interface guide; this may be a display identifier rather than a
  stable database key.
- Auto-number and metadata fields exist in interfaces, but their portability and
  uniqueness across environments are not confirmed.

Stable internal IDs, human-readable business numbers and source-file IDs should
be documented separately before migration or API integration.

## Conflicting or missing model definitions

1. **Offer terminology.** Legacy material uses `Offer`; current operational
   pages distinguish an SO document from SOL rows.
2. **DR.** Named as a model/process element in the system map but not defined
   as a table, document or state in the reviewed sources or owner decisions.
3. **Finance and payments.** Pricing variables and DDP outputs are documented,
   but Payment IN/OUT, billing, exchange-rate and reconciliation entities are
   not sufficiently defined here.
4. **Cardinality and deletion.** No approved source defines required versus
   optional links, cascade behavior, immutable snapshots or archive semantics.
5. **Vertical model.** Electronics and Clothing have functional parity except
   for the approved PO supplier rule: Electronics may have multiple suppliers,
   Clothing exactly one.

## Remaining model limitations

Exact field-level required/optional rules, cascade behavior and exceptional
deletion procedures still require schema inspection. They are not inferred from
the owner's statement that records normally remain in Airtable.

## Evidence and related drafts

- [[projects/svmpx/04-source-register/sources/supporting/core/system-002-1|System 002.1 outline]]
- [[projects/svmpx/04-source-register/sources/system-documentation-map|System documentation map]]
- [[projects/svmpx/04-source-register/sources/documentation/products-overview|Products overview]]
- [[projects/svmpx/04-source-register/sources/documentation/product-card|Product card]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-overview|Source Offers overview]]
- [[projects/svmpx/04-source-register/sources/documentation/source-offers-card|Source Offer line card]]
- [[projects/svmpx/04-source-register/sources/documentation/client-request|Client Request]]
- [[projects/svmpx/04-source-register/sources/documentation/client-proposal-workflow|Client Proposal workflow]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-order-overview|Purchase Order overview]]
- [[projects/svmpx/04-source-register/sources/documentation/purchase-orders-interface|Purchase Order interface]]
- [[projects/svmpx/04-source-register/sources/documentation/shipments-overview|Shipments overview]]
- [[projects/svmpx/00-canon/project-overview|Project overview draft]]
- [[projects/svmpx/00-canon/system-documentation|System documentation draft]]
- [[projects/svmpx/00-canon/ddp-finance-flow|DDP and finance flow draft]]
