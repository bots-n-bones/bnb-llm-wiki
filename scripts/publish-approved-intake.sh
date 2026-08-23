#!/usr/bin/env sh
set -eu

ROOT=${1:-/var/lib/docker/volumes/hermes-codex-workspace_hermes-knowledge/_data/bnb-llm-wiki}
STAGING=${2:-/var/lib/docker/volumes/hermes-codex-workspace_hermes-agent-data/_data/knowledge-intake}
DEPLOY_KEY=${BNB_WIKI_DEPLOY_KEY:-/root/.ssh/bnb-wiki-deploy}
VALIDATOR_IMAGE=${BNB_WIKI_VALIDATOR_IMAGE:-hermes-codex-workspace:server}

test -d "$ROOT/.git"
test -d "$STAGING"
test -r "$DEPLOY_KEY"

export GIT_SSH_COMMAND="ssh -i $DEPLOY_KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"

git -C "$ROOT" fetch origin main
git -C "$ROOT" reset --hard origin/main
git -C "$ROOT" clean -fd -- projects
python3 "$ROOT/scripts/manage-intake.py" materialize --staging "$STAGING" --repo "$ROOT"

git -C "$ROOT" add projects
if git -C "$ROOT" diff --cached --quiet; then
  exit 0
fi

INDEX_HOLD="$ROOT/.local-index"
mkdir -p "$INDEX_HOLD"
restore_index() {
  for name in knowledge.sqlite knowledge.sqlite.previous; do
    if [ -f "$INDEX_HOLD/$name" ]; then
      mv "$INDEX_HOLD/$name" "$ROOT/$name"
    fi
  done
}
rollback() {
  code=$?
  trap - EXIT HUP INT TERM
  restore_index
  if [ "$code" -ne 0 ]; then
    git -C "$ROOT" reset --hard origin/main >/dev/null 2>&1 || true
    git -C "$ROOT" clean -fd -- projects >/dev/null 2>&1 || true
  fi
  exit "$code"
}
trap rollback EXIT HUP INT TERM
for name in knowledge.sqlite knowledge.sqlite.previous; do
  if [ -f "$ROOT/$name" ]; then
    mv "$ROOT/$name" "$INDEX_HOLD/$name"
  fi
done
docker run --rm --entrypoint /bin/sh -v "$ROOT:/repo" -w /repo "$VALIDATOR_IMAGE" -lc 'npm ci >/dev/null && npm run validate'
restore_index
trap - EXIT HUP INT TERM
git -C "$ROOT" config user.name "Hermes Knowledge Bot"
git -C "$ROOT" config user.email "bots-n-bones@users.noreply.github.com"
git -C "$ROOT" commit -m "knowledge: publish approved intake drafts"
git -C "$ROOT" push git@github.com:bots-n-bones/bnb-llm-wiki.git HEAD:main
/bin/sh "$ROOT/scripts/sync-server-release.sh" "$ROOT"
