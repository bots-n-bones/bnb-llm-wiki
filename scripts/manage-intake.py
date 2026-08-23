#!/usr/bin/env python3
"""Stage notes, review pending intake, and materialize approved Wiki drafts."""

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(?:api[_ -]?key|secret|password|token)\s*[:=]\s*[^\s]{12,}"),
)
PROJECTS = ("svmpx", "hello-i-am", "content-os", "bots-n-bones", "quntm", "ursus", "shared")


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slug(value):
    value = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return value[:72] or "untitled"


def atomic_write(path, content, mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True)
    owner = path.stat() if path.exists() else path.parent.stat()
    with tempfile.NamedTemporaryFile(prefix=f".{path.name}.", dir=path.parent, delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(content)
        temporary = Path(tmp.name)
    os.chmod(temporary, mode)
    if os.geteuid() == 0:
        os.chown(temporary, owner.st_uid, owner.st_gid)
    os.replace(temporary, path)


def packages(staging):
    return sorted((staging / "pending").glob("*.json"))


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def find_package(staging, intake_id):
    matches = [(path, load(path)) for path in packages(staging)]
    exact = [(path, item) for path, item in matches if item.get("intake_id") == intake_id or item.get("drive_file_id") == intake_id]
    if len(exact) != 1:
        raise SystemExit(f"Expected one intake package for {intake_id!r}, found {len(exact)}")
    return exact[0]


def yaml_string(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def yaml_array(values):
    return json.dumps(list(values), ensure_ascii=False)


def source_frontmatter(item, source_id, project, captured_at):
    source = item["source"]
    return f'''---
schema: hermes-kb/v2
id: {source_id}
title: {yaml_string("Source: " + item["title"])}
project: {project}
type: source-record
status: active
canonical: false
owner: ilya
confidentiality: {item.get("confidentiality", "internal")}
summary: {yaml_string("Registered source from the governed Hermes intake pipeline.")}
created: {captured_at[:10]}
updated: {captured_at[:10]}
tags: {yaml_array(["inbox", "source", "google-drive" if item.get("drive_file_id") else "hermes-message"])}
source:
  kind: {yaml_string("google-drive" if item.get("drive_file_id") else "hermes-message")}
  drive_file_id: {yaml_string(item.get("drive_file_id") or item["intake_id"])}
  url: {yaml_string(source.get("url") or "https://hermes.molotilka.site/")}
  parent_folder_id: {yaml_string((source.get("parent_ids") or ["hermes-chat"])[0])}
  original_path: {yaml_string(source.get("original_path") or "Hermes chat message")}
  original_title: {yaml_string(item["title"])}
  mime_type: {yaml_string(source.get("mime_type") or "text/plain")}
  modified_time: {yaml_string(source.get("modified_time") or captured_at)}
  checksum: {yaml_string("sha256:" + item["extract_sha256"]) if item.get("extract_sha256") else "null"}
  revision_id: {yaml_string(str(source.get("drive_version"))) if source.get("drive_version") is not None else "null"}
---

# Source: {item["title"]}

## Provenance

- Intake ID: `{item["intake_id"]}`
- Original path: `{source.get("original_path") or "Hermes chat message"}`
- Captured: `{item.get("captured_at")}`
- Extraction: `{item.get("extraction_status")}`

## Authority

This page registers supporting evidence. It does not override active canon.
'''


def derived_frontmatter(item, source_id, derived_id, project, captured_at):
    text = item.get("extracted_text", "")[:120_000]
    return f'''---
schema: hermes-kb/v2
id: {derived_id}
title: {yaml_string(item["title"] + " — intake draft")}
project: {project}
type: derived
status: draft
canonical: false
owner: ilya
confidentiality: {item.get("confidentiality", "internal")}
summary: {yaml_string("Unreviewed text extracted from a registered intake source.")}
source_ids: {yaml_array([source_id])}
created: {captured_at[:10]}
updated: {captured_at[:10]}
tags: {yaml_array(["inbox", "derived", "needs-review"])}
derived:
  method: {yaml_string("drive-inbox-intake" if item.get("drive_file_id") else "hermes-message-intake")}
  generated_at: {yaml_string(captured_at)}
  extractor_version: "1"
---

# {item["title"]} — intake draft

> This is an unreviewed draft. It cannot override active canonical knowledge.

## Extracted content

{text}
'''


def stage_note(args):
    staging = Path(args.staging).resolve()
    captured_at = now()
    intake_id = "message-" + uuid.uuid4().hex
    text = args.text
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    item = {
        "schema": "hermes-kb-intake/v1", "intake_id": intake_id, "drive_file_id": None,
        "title": args.title, "project": args.project, "confidentiality": args.confidentiality,
        "status": "pending-review", "extraction_status": "extracted", "extraction_note": None,
        "extracted_text": text, "extract_sha256": digest, "captured_at": captured_at,
        "fingerprint": digest, "source": {"kind": "hermes-message", "url": "https://hermes.molotilka.site/",
        "original_path": "Hermes chat message", "mime_type": "text/plain", "modified_time": captured_at,
        "parent_ids": ["hermes-chat"]}, "publication_approved_at": None,
        "publication_approved_by": None, "materialized_at": None,
    }
    path = staging / "pending" / f"{slug(args.title)}-{intake_id[-12:]}.json"
    atomic_write(path, json.dumps(item, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "staged", "intake_id": intake_id, "path": str(path)}, ensure_ascii=False))


def list_items(args):
    staging = Path(args.staging).resolve()
    result = []
    for path in packages(staging):
        item = load(path)
        result.append({key: item.get(key) for key in ("intake_id", "title", "project", "status", "extraction_status", "publication_approved_at", "materialized_at")})
    print(json.dumps(result, ensure_ascii=False, indent=2))


def decide(args, decision):
    staging = Path(args.staging).resolve()
    path, item = find_package(staging, args.id)
    if decision == "approve":
        item["publication_approved_at"] = now()
        item["publication_approved_by"] = args.by
        item["status"] = "approved-for-publication"
    else:
        item["status"] = "rejected"
        item["review_note"] = args.note
    atomic_write(path, json.dumps(item, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": item["status"], "intake_id": item["intake_id"]}, ensure_ascii=False))


def reclassify(args):
    staging = Path(args.staging).resolve()
    path, item = find_package(staging, args.id)
    prior = item.get("project")
    item["project"] = args.project
    item["classification_note"] = args.note
    item["classified_at"] = now()
    atomic_write(path, json.dumps(item, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "reclassified", "intake_id": item["intake_id"], "from": prior, "to": args.project}, ensure_ascii=False))


def materialize(args):
    staging = Path(args.staging).resolve()
    repo = Path(args.repo).resolve()
    selected = []
    for path in packages(staging):
        item = load(path)
        materialized_paths = [repo / value for value in item.get("materialized_paths", [])]
        materialized_present = bool(materialized_paths) and all(value.exists() for value in materialized_paths)
        if item.get("publication_approved_at") and not materialized_present:
            if args.id and item.get("intake_id") != args.id and item.get("drive_file_id") != args.id:
                continue
            selected.append((path, item))
    written = []
    for path, item in selected:
        text = item.get("extracted_text", "")
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            item["status"] = "quarantined"
            item["review_note"] = "secret scanner blocked publication"
            atomic_write(path, json.dumps(item, ensure_ascii=False, indent=2) + "\n")
            continue
        project = item.get("project") if item.get("project") in PROJECTS else "shared"
        identity = str(item.get("drive_file_id") or item["intake_id"])
        key = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
        base = slug(item["title"])
        source_id = f"src-intake-{project}-{key}"
        derived_id = f"kb-intake-{project}-{key}"
        captured_at = item.get("captured_at") or now()
        source_path = repo / "projects" / project / "04-source-register" / "inbox" / f"{base}-{key}.md"
        atomic_write(source_path, source_frontmatter(item, source_id, project, captured_at), mode=0o644)
        written.append(str(source_path.relative_to(repo)))
        if text.strip():
            derived_path = repo / "projects" / project / "01-knowledge" / "inbox" / f"{base}-{key}.md"
            atomic_write(derived_path, derived_frontmatter(item, source_id, derived_id, project, captured_at), mode=0o644)
            written.append(str(derived_path.relative_to(repo)))
        item["status"] = "materialized-draft"
        item["materialized_at"] = now()
        item["materialized_paths"] = written[-2:] if text.strip() else written[-1:]
        atomic_write(path, json.dumps(item, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "materialized", "package_count": len(selected), "written": written}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--staging", required=True)
    note = sub.add_parser("stage-note")
    note.add_argument("--staging", required=True)
    note.add_argument("--project", required=True, choices=PROJECTS)
    note.add_argument("--title", required=True)
    note.add_argument("--text", required=True)
    note.add_argument("--confidentiality", choices=("public", "internal", "restricted"), default="internal")
    approve = sub.add_parser("approve")
    approve.add_argument("--staging", required=True)
    approve.add_argument("--id", required=True)
    approve.add_argument("--by", default="ilya")
    reject = sub.add_parser("reject")
    reject.add_argument("--staging", required=True)
    reject.add_argument("--id", required=True)
    reject.add_argument("--note", required=True)
    reclassify_parser = sub.add_parser("reclassify")
    reclassify_parser.add_argument("--staging", required=True)
    reclassify_parser.add_argument("--id", required=True)
    reclassify_parser.add_argument("--project", required=True, choices=PROJECTS)
    reclassify_parser.add_argument("--note", required=True)
    materialize_parser = sub.add_parser("materialize")
    materialize_parser.add_argument("--staging", required=True)
    materialize_parser.add_argument("--repo", required=True)
    materialize_parser.add_argument("--id")
    args = parser.parse_args()
    if args.command == "list": list_items(args)
    elif args.command == "stage-note": stage_note(args)
    elif args.command == "approve": decide(args, "approve")
    elif args.command == "reject": decide(args, "reject")
    elif args.command == "reclassify": reclassify(args)
    else: materialize(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
