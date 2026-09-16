@echo off
setlocal
cd /d "%~dp0"
for /f "usebackq delims=" %%i in (`py -3.12 scripts\env\select_venv.py --print`) do set "VENV_PATH=%%i"
if not defined VENV_PATH (
  echo Run setup-windows.bat first.
  exit /b 1
)
cd apps\desktop
"%VENV_PATH%\Scripts\python.exe" main.py

