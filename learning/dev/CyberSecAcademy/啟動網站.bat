@echo off
chcp 65001 >nul
title 資安自學院 CyberSec Academy
cd /d "%~dp0"
echo 正在啟動資安自學院...
py -3.13 -m pip install flask --quiet
start "" http://127.0.0.1:5000
py -3.13 app.py
pause
