#!/usr/bin/env python3
"""Build a portable, read-only SQLite FTS index from governed Wiki Markdown."""

import argparse
import json
import os
import re
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_markdown(path: Path, root: Path):
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", raw, re.DOTALL)
    if not match:
        return None
    header, body = match.groups()
    metadata: dict[str, str] = {}
    for line in header.splitlines():
        item = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if item:
            metadata[item.group(1)] = scalar(item.group(2))
    required = ("id", "title", "status", "type", "canonical")
    if any(not metadata.get(key) for key in required):
        return None
    canonical = metadata.get("canonical", "false").casefold() == "true"
    status = metadata["status"]
    if canonical and status == "active":
        tier, rank = "active-canonical", 1
    elif status == "active":
        tier, rank = "active-source", 2
    elif status in {"superseded", "archived", "quarantined"}:
        tier, rank = status, 5
    else:
        tier, rank = "draft", 3
    routing = " ".join((metadata.get("title", ""), metadata.get("summary", ""), body))
    return {
        "document_id": metadata["id"],
        "title": metadata["title"],
        "project": metadata.get("project"),
        "status": status,
        "document_type": metadata["type"],
        "body": body,
        "wiki_path": path.relative_to(root).as_posix(),
        "tier": tier,
        "tier_rank": rank,
        "routing_text": routing,
    }


def build(root: Path, output: Path) -> int:
    records = []
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "node_modules", ".local-index"} for part in path.parts):
            continue
        record = parse_markdown(path, root)
        if record:
            records.append(record)
    if not records:
        raise RuntimeError("No governed Markdown documents found.")

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix="knowledge-", suffix=".sqlite", dir=output.parent, delete=False) as tmp:
        temporary = Path(tmp.name)
    try:
        with sqlite3.connect(temporary) as db:
            db.executescript("""
              PRAGMA journal_mode=DELETE;
              CREATE TABLE documents (
                document_id TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                project TEXT,
                status TEXT NOT NULL,
                document_type TEXT,
                body TEXT NOT NULL,
                wiki_path TEXT NOT NULL UNIQUE,
                tier TEXT NOT NULL,
                tier_rank INTEGER NOT NULL,
                routing_text TEXT NOT NULL
              );
              CREATE VIRTUAL TABLE documents_fts USING fts5(normalized);
            """)
            for record in records:
                cursor = db.execute(
                    """INSERT INTO documents
                      (document_id,title,project,status,document_type,body,wiki_path,tier,tier_rank,routing_text)
                      VALUES (:document_id,:title,:project,:status,:document_type,:body,:wiki_path,:tier,:tier_rank,:routing_text)""",
                    record,
                )
                normalized = re.sub(r"[^\w]+", " ", record["routing_text"].casefold(), flags=re.UNICODE)
                db.execute("INSERT INTO documents_fts(rowid, normalized) VALUES (?, ?)", (cursor.lastrowid, normalized))
            db.commit()
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({"database": str(output), "documentCount": len(records), "publishedAt": datetime.now(timezone.utc).isoformat()}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--out", default="knowledge.sqlite")
    args = parser.parse_args()
    return build(Path(args.root).resolve(), Path(args.out).resolve())


if __name__ == "__main__":
    sys.exit(main())
