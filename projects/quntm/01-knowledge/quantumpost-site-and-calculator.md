---
schema: hermes-kb/v2
id: kb-quntm-quantumpost-site-and-calculator
title: QuantumPost site and calculator requirements
project: quntm
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
summary: Каноническое описание сайта QuantumPost/QP Rail Express и логики калькулятора доставки.
source_ids: ["src-intake-quntm-24bb6d0c1abf221f"]
created: 2026-08-23
updated: 2026-08-23
tags: ["quantumpost", "calculator", "rail-express", "site"]
---

# QuantumPost site and calculator requirements

## Site structure

QuantumPost presents QP Rail Express as the primary service and includes QP AVIA EXPRESS and QP TIR EXPRESS as service blocks; AVIA and TIR may be visually marked as future/soon-to-launch services.

The site should include cargo tracking in the header, a personal-account entry point, a rotating news/promotional banner, service cards, and explanatory blocks for delivery of consolidated cargo, cargo transportation, international delivery from China, and warehousing services.

## QP Rail Express positioning

QP Rail Express is positioned as premium high-speed China–Russia rail logistics on the Hunchun–Moscow route, with an advertised delivery target of 8.5–9 days, fixed/regular dispatches, cargo monitoring, seal-integrity sensors, video surveillance, and professional support.

## Calculator logic

The delivery calculator covers three transport modes: Rail Express, auto, and avia. Rail Express is the described active calculation flow; auto and avia are marked as in progress in the source.

For Rail Express, the cost structure is:

`ИТОГО = первая миля до Хуньчуня + ж/д фрахт Хуньчунь → Москва + дополнительные услуги`

The calculator inputs include route origin in China, Moscow as destination, optional Moscow/MO last-mile delivery, cargo weight, volume, number of pieces, cargo type, and additional services such as certification, packing/palletizing, Russian customs clearance, and insurance.

## Review note

This page records owner-approved product and calculator requirements. Detailed first-mile tariffs are maintained separately in `projects/quntm/01-knowledge/first-mile-calculator.md`.
