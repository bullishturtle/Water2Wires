@echo off
title Water2Wires Launcher
color 0B
echo.
echo  ╔═══════════════════════════════════════════════════════════════╗
echo  ║           WATER2WIRES - Data Recovery + Optimizer              ║
echo  ║                      Launch Sequence                           ║
echo  ╚═══════════════════════════════════════════════════════════════╝
echo.
echo  [*] Starting Water2Wires services...
echo.

:: Check if Python is available
where python >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo  [!] Python not found. Installing dependencies may fail.
    echo  [!] Please install Python 3.8+ from python.org
    goto :START_FRONTEND
)

:: Start the API server in background
echo  [*] Starting API server on port 8742...
start /min cmd /c "cd /d %~dp0 && python src/api/server.py"
timeout /t 2 /nobreak >nul

:START_FRONTEND
:: Start the frontend
echo  [*] Starting frontend...
echo.

:: Check if node_modules exists
if not exist "node_modules\" (
    echo  [*] Installing dependencies (first run)...
    call npm install
)

:: Start development server
echo  [*] Opening Water2Wires in browser...
echo.
echo  ═══════════════════════════════════════════════════════════════
echo   Water2Wires is running!
echo   Local:   http://localhost:1420
echo   API:     http://localhost:8742
echo   
echo   Press Ctrl+C to stop
echo  ═══════════════════════════════════════════════════════════════
echo.

call npm run dev

:: Cleanup when user stops
echo.
echo  [*] Shutting down Water2Wires...
taskkill /f /fi "WINDOWTITLE eq Water2Wires API*" >nul 2>&1
echo  [*] Done!
pause

