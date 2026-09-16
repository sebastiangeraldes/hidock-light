#!/bin/bash
# Direct launcher for HiDock Light from app directory
echo "Launching HiDock Light..."
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
exec "$ROOT_DIR/run-desktop.sh"
