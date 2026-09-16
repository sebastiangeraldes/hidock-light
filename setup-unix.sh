#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_PATH="$($PYTHON_BIN "$ROOT_DIR/scripts/env/select_venv.py" --ensure --print)"
"$VENV_PATH/bin/python" -m pip install -e "$ROOT_DIR/apps/desktop[dev]"
echo "HiDock Light is ready. Run ./run-desktop.sh"

