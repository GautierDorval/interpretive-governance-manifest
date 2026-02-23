#!/usr/bin/env bash
set -euo pipefail

MODE="build"
if [[ "${1:-}" == "--check" ]]; then
  MODE="check"
fi

if [[ ! -f "./scripts/requirements.txt" ]]; then
  echo "Run this script from the repository root." >&2
  exit 2
fi

python -m pip install --upgrade pip >/dev/null
python -m pip install -r ./scripts/requirements.txt >/dev/null

if [[ "$MODE" == "check" ]]; then
  python ./scripts/generate_entity_graph.py --check
  python ./scripts/recompute_integrity_hashes.py --check
  echo "✅ Check OK."
  exit 0
fi

python ./scripts/generate_entity_graph.py
python ./scripts/recompute_integrity_hashes.py
echo "✅ Build complete. Review changes, then commit."
