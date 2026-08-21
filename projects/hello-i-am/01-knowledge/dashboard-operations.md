---
schema: hermes-kb/v2
id: kb-hello-i-am-dashboard-operations
title: "Hello I Am local dashboard operations"
project: hello-i-am
type: canon
status: active
canonical: true
owner: ilya
confidentiality: internal
created: 2026-08-20
updated: 2026-08-20
tags: [dashboard, operations]
aliases:
  - "Локальный запуск dashboard Hello I Am"
  - "Разделы дашборда Hello I Am"
  - "Операции локального дашборда"
summary: "Как локально запускается dashboard Hello I Am, какие страницы, папки и API ему нужны, и чем отличается правильный сервер."
source_ids:
  - kb-hello-i-am-source-dashboard-readme
derived:
  method: local-read-only-portfolio-curation
  generated_at: "2026-08-20T00:00:00Z"
  extractor_version: null
---

# Hello I Am local dashboard operations

## Purpose

The dashboard is an internal interface for brand documents, version history, Instagram analytics, and a Post Lab.

## Local runtime

The source requires Python 3.10+ and its dedicated `dev_server.py`. The documented default URL uses port 8766; a generic static HTTP server is insufficient because analytics and Post Lab depend on local API routes.

## Main surfaces

- Main index for files, versions, analytics, and technical information.
- Document viewer for brand and canon materials.
- Post Lab for local image upload and layout generation using brand rules.
- Instagram sync/edit/export flow backed by live API or an offline snapshot.

## Repository dependencies

The dashboard expects sibling brand, analytics, and system-version folders. Assets and links are optional. This draft records the documented local topology; it does not start services or contact Instagram.
