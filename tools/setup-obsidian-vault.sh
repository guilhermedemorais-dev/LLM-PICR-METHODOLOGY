#!/usr/bin/env bash
set -euo pipefail

VAULT_PATH="${1:-}"

if [[ -z "$VAULT_PATH" ]]; then
  echo "usage: bash tools/setup-obsidian-vault.sh <vault-path>"
  exit 1
fi

mkdir -p "$VAULT_PATH"
python3 tools/export-obsidian.py "$VAULT_PATH"

echo
echo "Obsidian vault prepared at: $VAULT_PATH"
echo "Open the vault in Obsidian and start from: PICR Home.md"
