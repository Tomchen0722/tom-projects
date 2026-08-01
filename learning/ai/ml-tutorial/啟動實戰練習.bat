@echo off
title ML Practice - Jupyter Notebook
cd /d "%~dp0"

set PY=C:\Users\USER\anaconda3\python.exe
if not exist "%PY%" set PY=python

echo.
echo   ==================================================
echo      ML Practice  -  Jupyter Notebook
echo   ==================================================
echo.
echo   Starting Jupyter... browser will open automatically.
echo.
echo   How to use:  click a code cell, press Shift + Enter
echo   Close this black window to stop.
echo.

"%PY%" -m notebook --notebook-dir="%~dp0notebooks"

echo.
echo   Jupyter stopped.
pause
