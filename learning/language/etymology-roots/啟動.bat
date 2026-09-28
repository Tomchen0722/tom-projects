@echo off
chcp 65001 >nul
title 字根字首魔法學院 EtymoRoots Master
echo ========================================================
echo   🌱 字根字首魔法學院 (EtymoRoots Master)
echo   正在為您啟動本機伺服器 http://127.0.0.1:7025 ...
echo ========================================================
start "" http://127.0.0.1:7025
python -m http.server 7025
pause
