#!/usr/bin/env sh
set -eu

CONTAINER=${HERMES_WORKSPACE_CONTAINER:-hermes-codex-workspace-hermes-workspace-1}

docker inspect "$CONTAINER" >/dev/null 2>&1
docker exec "$CONTAINER" sh -lc '
set -eu
work=$(mktemp -d)
trap "rm -rf $work" EXIT HUP INT TERM
node -e "process.stdout.write(JSON.stringify({password: process.env.HERMES_PASSWORD || \"\"}))" > "$work/auth.json"
curl -fsS -c "$work/cookies" -H "content-type: application/json" \
  --data-binary @"$work/auth.json" http://127.0.0.1:3000/api/auth >/dev/null
curl -fsS -X POST -b "$work/cookies" \
  http://127.0.0.1:3000/api/knowledge/sync > "$work/result.json"
node -e "const fs=require(\"fs\"); const p=JSON.parse(fs.readFileSync(process.argv[1],\"utf8\")); if(!p.success || !p.index || !p.index.releaseId) process.exit(1); process.stdout.write(JSON.stringify(p));" \
  "$work/result.json"
'
