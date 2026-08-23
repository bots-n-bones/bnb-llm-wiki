#!/usr/bin/env sh
set -eu

ROOT=${1:-/opt/knowledge/bnb-llm-wiki}
DEPLOY_KEY=${BNB_WIKI_DEPLOY_KEY:-/root/.ssh/bnb-wiki-deploy}
DATABASE="$ROOT/knowledge.sqlite"
PREVIOUS_DATABASE="$ROOT/knowledge.sqlite.previous"
PREVIOUS_REF=$(git -C "$ROOT" rev-parse HEAD)

test -r "$DEPLOY_KEY"
export GIT_SSH_COMMAND="ssh -i $DEPLOY_KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"

if [ -f "$DATABASE" ]; then
  cp -p "$DATABASE" "$PREVIOUS_DATABASE"
fi

rollback() {
  code=$?
  trap - EXIT HUP INT TERM
  if [ "$code" -ne 0 ]; then
    git -C "$ROOT" reset --hard "$PREVIOUS_REF" >/dev/null 2>&1 || true
    if [ -f "$PREVIOUS_DATABASE" ]; then
      cp -p "$PREVIOUS_DATABASE" "$DATABASE" || true
    fi
  fi
  exit "$code"
}
trap rollback EXIT HUP INT TERM

git -C "$ROOT" fetch origin main
git -C "$ROOT" reset --hard origin/main
python3 "$ROOT/scripts/rebuild-index.py" --root "$ROOT" --out "$DATABASE"
python3 - "$DATABASE" <<'PY'
import os
import stat
import sys

mode = stat.S_IMODE(os.stat(sys.argv[1]).st_mode)
if mode & 0o044 != 0o044:
    raise SystemExit(f"published index is not world-readable: {oct(mode)}")
PY
python3 "$ROOT/scripts/query-index.py" "DDP" --db "$DATABASE" --limit 1 >/dev/null
trap - EXIT HUP INT TERM
