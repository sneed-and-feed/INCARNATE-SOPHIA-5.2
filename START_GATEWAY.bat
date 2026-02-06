@echo off
title Grok Relay Gateway [PORT 11434]
color 0A
cd /d "%~dp0"

echo ==================================================
echo   SOPHIA SOVEREIGN // GROK RELAY GATEWAY
echo ==================================================
echo.

:: 1. Check for Virtual Environment
if exist ".venv\Scripts\python.exe" (
    echo [*] Virtual Environment Detected. Using .venv...
    set "PYTHON_CMD=.venv\Scripts\python.exe"
) else (
    echo [!] No .venv found. Using system Python...
    set "PYTHON_CMD=python"
)

:: 2. Launch Relay
echo [*] Launching engine/grok_relay.py...
echo.
"%PYTHON_CMD%" engine/grok_relay.py

:: 3. Handle Exit
if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo.
    echo [!] CRITICAL ERROR: The relay process exited with error code %ERRORLEVEL%.
) else (
    echo.
    echo [*] Relay process exited normally.
)

echo.
echo Press any key to close this window...
pause >nul
