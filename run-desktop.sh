#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_PATH="$($PYTHON_BIN "$ROOT_DIR/scripts/env/select_venv.py" --print)"
if [[ ! -x "$VENV_PATH/bin/python" ]]; then
  echo "Run ./setup-unix.sh first." >&2
  exit 1
fi
cd "$ROOT_DIR/apps/desktop"
exec "$VENV_PATH/bin/python" main.py

