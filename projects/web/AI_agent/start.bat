@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ======================================
echo   自動的小龍蝦 AI 指揮室 啟動中...
echo ======================================
set PY=py
where py >nul 2>nul || set PY=python
%PY% -c "import flask" 2>nul
if errorlevel 1 (
  echo 首次執行，安裝 Flask...
  %PY% -m pip install flask
)
start "" http://localhost:5566
%PY% app.py
pause
