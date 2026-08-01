@echo off
title AI Learning Map
cd /d "%~dp0"

set PY=C:\Users\USER\anaconda3\python.exe
if not exist "%PY%" set PY=python

echo.
echo   ==================================================
echo      AI Learning Map  /  AI Xue Xi Di Tu
echo   ==================================================
echo.
echo   Starting... browser will open automatically.
echo   URL:  http://localhost:8510
echo.
echo   Close this black window to stop the app.
echo.

"%PY%" -m streamlit run app.py --server.port 8510

echo.
echo   App stopped.
pause
