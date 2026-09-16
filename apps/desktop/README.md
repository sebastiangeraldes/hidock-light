# HiDock Light desktop app

This directory contains the Python desktop application distributed as HiDock Light.

## Run locally

From the repository root, use the platform setup and launch scripts described in the [main README](../../README.md).

For development with an existing environment:

```bash
python -m pip install -e ".[dev]"
python -m pytest tests -m "not integration and not gui and not slow" --no-cov
python main.py
```

## Scope

HiDock Light provides direct device management, recording downloads, local playback, storage controls, and the lightweight transcription workflow. The full knowledge workspace is maintained separately in [HiDock Next 2.0](https://github.com/sgeraldes/hidock-next-2).

## Device safety

All USB changes must be exercised with mocks before any controlled hardware validation. Do not run exploratory probes, rapid connection loops, or concurrent USB stacks against a connected device.
