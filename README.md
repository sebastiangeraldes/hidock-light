# HiDock Light

HiDock Light is the focused Python desktop app for people who want direct HiDock device management without the knowledge workspace included in HiDock Next 2.0.

Use it to connect supported HiDock devices, browse recordings, download files, manage storage, and run the original lightweight transcription workflow.

> Want the full library, calendar, people, projects, action items, search, and knowledge graph? Use [HiDock Next 2.0](https://github.com/sgeraldes/hidock-next-2).

## Install

Python 3.11 or 3.12 is recommended.

### Windows

```bat
setup-windows.bat
run-desktop.bat
```

### macOS and Linux

```bash
./setup-unix.sh
./run-desktop.sh
```

macOS users may need `brew install libusb`. Linux users may need distribution-specific USB permissions.

## Development

```bash
python scripts/env/select_venv.py --ensure --print
python -m pytest apps/desktop/tests
```

All device work must be mock-tested first. Never run exploratory USB scripts or repeated open/close probes against a connected HiDock device.

## Community fixes carried forward

- Ubuntu launcher, USB diagnostics, and high-DPI tree responsiveness from [@asyouplz](https://github.com/asyouplz), original PR [#48](https://github.com/sgeraldes/hidock-next/pull/48).
- Shift-click range selection and multi-select default from [@blindbatts](https://github.com/blindbatts), original PR [#52](https://github.com/sgeraldes/hidock-next/pull/52).
- H1 `0xB00C` product ID support from [@gausin3](https://github.com/gausin3), original PR [#82](https://github.com/sgeraldes/hidock-next/pull/82).
- P1 version-5 duration behavior based on hardware findings from [@fjbravo](https://github.com/fjbravo) in issue [#24](https://github.com/sgeraldes/hidock-next/issues/24).

MIT licensed. HiDock is a trademark of its respective owner. This community project is not affiliated with or endorsed by HiDock.
