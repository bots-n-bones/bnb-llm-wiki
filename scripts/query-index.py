#!/usr/bin/env python3
"""Read-only retrieval from a released BnB Wiki SQLite FTS index."""

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path


def fts_query(text: str) -> str:
    terms = re.findall(r"[\w\-]+", text, flags=re.UNICODE)
    stop_words = {"как", "что", "где", "когда", "почему", "ли", "и", "в", "на", "по", "с", "о", "от", "для", "это", "the", "a", "an"}
    terms = [term for term in terms if term.casefold() not in stop_words]
    if not terms:
        raise ValueError("Query must contain at least one word.")
    return " OR ".join(f'"{term.replace(chr(34), "")}"*' for term in terms)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--db", default="knowledge.sqlite")
    parser.add_argument("--project")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    db = Path(args.db)
    if not db.is_file():
        print(json.dumps({"error": f"Index not found: {db}"}), file=sys.stderr)
        return 2

    try:
        match = fts_query(args.query)
    except ValueError as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2

    sql = """
      SELECT d.document_id, d.title, d.project, d.status, d.document_type,
             d.wiki_path, d.tier,
             snippet(documents_fts, 0, '[', ']', '…', 24) AS snippet,
             bm25(documents_fts) AS relevance
      FROM documents_fts
      JOIN documents d ON d.rowid = documents_fts.rowid
      WHERE documents_fts MATCH :match
        AND (:project IS NULL OR d.project = :project)
      ORDER BY d.tier_rank ASC, relevance ASC
      LIMIT :limit
    """
    with sqlite3.connect(db) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            sql,
            {"match": match, "project": args.project, "limit": max(1, min(args.limit, 20))},
        ).fetchall()
    print(json.dumps([dict(row) for row in rows], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
