@echo off
chcp 65001 >nul
title AWS SAA-C03 學習中心
echo ============================================
echo   AWS SAA-C03 學習中心 啟動中...
echo   關閉此視窗即停止伺服器
echo ============================================
cd /d "%~dp0"
start "" http://localhost:8866/index.html
where python >nul 2>nul
if %errorlevel%==0 (
  python -m http.server 8866
) else (
  where py >nul 2>nul
  if %errorlevel%==0 (
    py -m http.server 8866
  ) else (
    echo.
    echo [提示] 找不到 Python，改用 npx serve（需已安裝 Node.js）...
    npx --yes serve -l 8866 .
  )
)
pause
