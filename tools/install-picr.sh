#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-}"
TARGET_DIR="${2:-}"

if [[ -z "$REPO_URL" ]]; then
  echo "usage: bash tools/install-picr.sh <repo-url> [target-dir]"
  exit 1
fi

if [[ -z "$TARGET_DIR" ]]; then
  TARGET_DIR="$(basename "$REPO_URL" .git)"
fi

git clone "$REPO_URL" "$TARGET_DIR"
cd "$TARGET_DIR"
python3 tools/build-index.py

echo
echo "PICR installed in: $(pwd)"
echo "Test with:"
echo "python3 tools/route.py \"I need a skill for Python API security review\""
