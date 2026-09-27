@echo off
chcp 65001 >nul
title 英文歌學英語 English Song Learning
echo ========================================================
echo   🎵 英文歌學英語系統 (English Song Learning)
echo   正在為您啟動本機伺服器...
echo ========================================================
start "" http://127.0.0.1:7020
python -m http.server 7020
pause
