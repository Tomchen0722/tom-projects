@echo off

pyinstaller ^
--clean ^
--noconfirm ^
--onefile ^
--windowed ^
--name AI_Meeting_Assistant ^
--icon assets\icon.ico ^
main.py

pause