@echo off
title STOP Grok Relay
color 0E
echo ==================================================
echo   STOPPING GROK RELAY GATEWAY
echo ==================================================
echo.

echo [*] Searching for processes on port 11434...

:: Find PID of process listening on 11434
for /f "tokens=5" %%a in ('netstat -aon ^| find ":11434" ^| find "LISTENING"') do (
    set PID=%%a
)

if defined PID (
    echo [*] Found process with PID: %PID%
    echo [*] Terminating...
    taskkill /F /PID %PID%
    echo.
    echo [OK] Gateway Stopped safely.
) else (
    echo [!] No active gateway found on port 11434.
    echo     (It might already be stopped)
)

echo.
timeout /t 3 >nul
