#!/usr/bin/env python3
"""Resolve and optionally ensure the correct per-platform virtual environment.

Usage:
    python scripts/env/select_venv.py --print        # print resolved path only
    python scripts/env/select_venv.py --ensure       # create if missing
    python scripts/env/select_venv.py --ensure --print
    python scripts/env/select_venv.py --activate-cmd # activation command

Decision order:
    1. Detect WSL ("microsoft" in kernel release)
    2. platform.system() in {Windows, Darwin, Linux}
    3. Fallback to .venv.linux for other Unix
    4. If legacy .venv exists and target does not, warn

Creation logic uses the current interpreter (sys.executable).
"""
from __future__ import annotations
import argparse
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # project root
DESKTOP_DIR = ROOT / "apps" / "desktop"
LEGACY = DESKTOP_DIR / ".venv"

PLATFORM_MAP = {
    "Windows": ".venv.win",
    "Darwin": ".venv.mac",
    "Linux": ".venv.wsl",  # will override for bare metal below
}


def detect_wsl() -> bool:
    release = platform.uname().release.lower()
    return "microsoft" in release


def resolve_target() -> Path:
    system = platform.system()
    if system == "Linux":
        if detect_wsl():
            name = ".venv.wsl"
        else:
            name = ".venv.linux"
    else:
        name = PLATFORM_MAP.get(system, ".venv.linux")
    return DESKTOP_DIR / name


def create_env(path: Path) -> bool:
    print(f"[select_venv] Creating virtual environment at {path}")
    result = subprocess.run(
        [sys.executable, "-m", "venv", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print("[select_venv] ERROR: Failed to create virtual environment")
        return False
    # Basic seed upgrade (best effort)
    scripts_dir = "Scripts" if platform.system() == "Windows" else "bin"
    py_name = "python.exe" if platform.system() == "Windows" else "python"
    python_bin = path / scripts_dir / py_name
    subprocess.run(
        [
            str(python_bin),
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
            "setuptools",
            "wheel",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return True


def activation_command(path: Path) -> str:
    if platform.system() == "Windows":
        return f"{path}\\Scripts\\activate"
    return f"source {path}/bin/activate"


def main() -> None:
    parser = argparse.ArgumentParser(description="Select per-platform venv")
    parser.add_argument("--print", action="store_true", help="Print the resolved path")
    parser.add_argument("--ensure", action="store_true", help="Create if missing")
    parser.add_argument("--activate-cmd", action="store_true", help="Print activation command")
    parser.add_argument("--quiet", action="store_true", help="Suppress non-essential output")
    args = parser.parse_args()

    target = resolve_target()

    if LEGACY.exists() and not target.exists() and not args.quiet:
        print(f"[select_venv] Legacy .venv detected at {LEGACY}. " f"Consider migrating to {target.name}.")

    if args.ensure and not target.exists():
        if not create_env(target):
            sys.exit(1)

    if args.print:
        print(str(target))

    if args.activate_cmd:
        print(activation_command(target))

    if not (args.print or args.activate_cmd) and not args.quiet:
        status = "present" if target.exists() else "missing"
        print(f"[select_venv] Resolved: {target} ({status})")


if __name__ == "__main__":
    main()
