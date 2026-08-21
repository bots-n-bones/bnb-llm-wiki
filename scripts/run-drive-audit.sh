#!/usr/bin/env sh
set -eu

REPO=${1:-/opt/knowledge/bnb-llm-wiki}
STAGING=${2:-/opt/data/knowledge-drive-audit}
FOLDER_ID=${BNB_DRIVE_ROOT_ID:-1VfCO8UnD0Qq4D6k-f-HTk7ELgy9j0XOg}
PYTHON=${GOOGLE_WORKSPACE_PYTHON:-/opt/data/.google-workspace-venv/bin/python}
TOKEN=${GOOGLE_DRIVE_TOKEN:-/opt/data/google_drive_readonly_token.json}

test -r "$REPO/scripts/drive-inbox-intake.py"
test -x "$PYTHON"
test -r "$TOKEN"

exec "$PYTHON" "$REPO/scripts/drive-inbox-intake.py" \
  --folder-id "$FOLDER_ID" \
  --folder-name "bots-n-bones" \
  --token "$TOKEN" \
  --staging "$STAGING" \
  --manifest-only \
  --bulk-list
