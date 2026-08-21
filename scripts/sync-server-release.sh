#!/usr/bin/env sh
set -eu

ROOT=${1:-/opt/knowledge/bnb-llm-wiki}

git -C "$ROOT" fetch origin main
git -C "$ROOT" reset --hard origin/main
python3 "$ROOT/scripts/rebuild-index.py" --root "$ROOT" --out "$ROOT/knowledge.sqlite"
python3 "$ROOT/scripts/query-index.py" "DDP" --db "$ROOT/knowledge.sqlite" --limit 1 >/dev/null
