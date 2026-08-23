#!/usr/bin/env sh
set -eu

CONTAINER=${HERMES_CONTAINER:-hermes-codex-workspace-hermes-agent-1}
REPO=${HERMES_KNOWLEDGE_REPO:-/opt/knowledge/bnb-llm-wiki}
STAGING=${HERMES_KNOWLEDGE_STAGING:-/opt/data/knowledge-intake}
PUBLIC_URL=${HERMES_PUBLIC_URL:-https://hermes.molotilka.site/}
HOST_REPO=${HERMES_KNOWLEDGE_HOST_REPO:-/var/lib/docker/volumes/hermes-codex-workspace_hermes-knowledge/_data/bnb-llm-wiki}
DEPLOY_KEY=${BNB_WIKI_DEPLOY_KEY:-/root/.ssh/bnb-wiki-deploy}

fail() {
  logger -t hermes-bnb-knowledge "FAILED: $*" 2>/dev/null || true
  echo "FAILED: $*" >&2
  exit 1
}

health=$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$CONTAINER" 2>/dev/null) || fail "container missing"
[ "$health" = healthy ] || fail "container health=$health"

docker exec -u hermes "$CONTAINER" test -r "$REPO/knowledge.sqlite" || fail "index unreadable by hermes"
docker exec -u hermes "$CONTAINER" python3 "$REPO/scripts/query-index.py" "DDP" --db "$REPO/knowledge.sqlite" --limit 1 >/dev/null || fail "retrieval smoke failed"
docker exec "$CONTAINER" sh -lc "curl -fsS http://127.0.0.1:8642/health >/dev/null" || fail "gateway health failed"
docker exec -u hermes "$CONTAINER" python3 /opt/data/skills/bnb-knowledge/scripts/query.py --query "DDP" --project svmpx --limit 1 >/dev/null || fail "published Wiki service smoke failed"

[ -r "$DEPLOY_KEY" ] || fail "GitHub deploy key unreadable"
GIT_SSH_COMMAND="ssh -i $DEPLOY_KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new" \
  git -C "$HOST_REPO" ls-remote --exit-code origin refs/heads/main >/dev/null || fail "GitHub release access failed"

if docker exec "$CONTAINER" test -f "$STAGING/health.json"; then
  docker exec -i -u hermes "$CONTAINER" python3 - "$STAGING/health.json" <<'PY' || fail "Drive intake unhealthy"
import json
import sys
from datetime import datetime, timezone

payload = json.load(open(sys.argv[1], encoding="utf-8"))
captured = datetime.fromisoformat(payload["captured_at"].replace("Z", "+00:00"))
age = (datetime.now(timezone.utc) - captured).total_seconds()
if age > 1800:
    raise SystemExit(f"Drive intake stale: {age:.0f}s")
if payload.get("error_count", 0):
    raise SystemExit(f"Drive intake errors: {payload['error_count']}")
PY
fi

curl -fsS --max-time 15 -o /dev/null "$PUBLIC_URL" || fail "public route failed"
echo "OK: container, gateway, published Wiki, GitHub release access, Drive intake and public route"
