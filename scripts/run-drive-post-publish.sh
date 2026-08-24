#!/bin/sh
set -eu

REPO=${HERMES_KNOWLEDGE_REPO:-/opt/knowledge/bnb-llm-wiki}
STAGING=${HERMES_KNOWLEDGE_STAGING:-/opt/data/knowledge-intake}
TOKEN=${HERMES_GOOGLE_TOKEN:-/opt/data/google_token.json}

exec /usr/bin/python3 "$REPO/scripts/move-published-drive-intake.py" \
  --staging "$STAGING" \
  --token "$TOKEN" \
  --destinations "$REPO/config/drive-project-destinations.json"
