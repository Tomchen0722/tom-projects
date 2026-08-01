@echo off
chcp 65001 >nul
REM 台股波段回測 — 打包成「資料夾版」(onedir)，啟動即開、不需每次解壓
REM 用法：在 Anaconda Prompt (base 環境) 進到專案根目錄後，執行本檔
cd /d %~dp0

pyinstaller --onedir --windowed --noconfirm --name 台股波段回測 --paths src ^
  --exclude-module PyQt5 --exclude-module PyQt6 --exclude-module PySide2 --exclude-module PySide6 ^
  --exclude-module matplotlib --exclude-module IPython ^
  --hidden-import backtest_runner --hidden-import data_source --hidden-import data_panel ^
  --hidden-import evaluation --hidden-import features_chip --hidden-import signals ^
  --hidden-import strategy_baseline --hidden-import config --hidden-import signal_quality ^
  --hidden-import longshort --hidden-import walkforward ^
  gui_app.py

echo.
echo ============================================================
echo 完成後，程式在資料夾： dist\台股波段回測\台股波段回測.exe
echo 雙擊該 exe 即可開啟(啟動即開)。整個資料夾要一起保留、不要只搬 exe。
echo ============================================================
pause
