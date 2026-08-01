@echo off
setlocal enabledelayedexpansion
title Tom Chen - Project Hub
cd /d "%~dp0"

rem ---------------------------------------------------------------
rem  This file is intentionally written in plain ASCII.
rem  cmd.exe reads .bat files using the system ANSI codepage (CP950
rem  on this machine), so UTF-8 Chinese characters would corrupt the
rem  commands themselves. Keep this file English-only.
rem ---------------------------------------------------------------

echo.
echo   ============================================================
echo      Tom Chen  ^|  Project Hub
echo   ============================================================
echo.

set "PY="
if exist "%USERPROFILE%\anaconda3\python.exe" set "PY=%USERPROFILE%\anaconda3\python.exe"
if not defined PY if exist "%USERPROFILE%\miniconda3\python.exe" set "PY=%USERPROFILE%\miniconda3\python.exe"
if not defined PY if exist "C:\ProgramData\anaconda3\python.exe" set "PY=C:\ProgramData\anaconda3\python.exe"

if not defined PY (
  where py >nul 2>nul
  if not errorlevel 1 set "PY=py"
)
if not defined PY (
  where python >nul 2>nul
  if not errorlevel 1 set "PY=python"
)

if not defined PY (
  echo   [ERROR] Python not found. Please install Python 3.11 or newer.
  echo.
  pause
  exit /b 1
)

echo   Python: !PY!

"!PY!" -c "import flask" >nul 2>nul
if errorlevel 1 (
  echo   Installing Flask ^(first run only^)...
  "!PY!" -m pip install flask --quiet
)

echo   Starting... your browser will open automatically.
echo   URL: http://127.0.0.1:7000
echo.
echo   Closing this window also stops every project you launched.
echo.

"!PY!" hub\app.py

echo.
echo   Hub stopped.
pause
