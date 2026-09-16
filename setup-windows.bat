@echo off
setlocal
cd /d "%~dp0"
for /f "usebackq delims=" %%i in (`py -3.12 scripts\env\select_venv.py --ensure --print`) do set "VENV_PATH=%%i"
if not defined VENV_PATH (
  echo Failed to create the Python environment. Install Python 3.12 and try again.
  exit /b 1
)
"%VENV_PATH%\Scripts\python.exe" -m pip install -e "apps\desktop[dev]"
exit /b %errorlevel%

