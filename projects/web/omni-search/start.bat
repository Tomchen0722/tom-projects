@echo off
chcp 65001 >nul
title OmniSearch 全球萬維搜尋引擎
cd /d "%~dp0"
echo =======================================================
echo   正在啟動 OmniSearch 全球萬維智慧搜尋引擎...
echo   本機網址: http://127.0.0.1:7050
echo =======================================================
python app.py
pause
