@echo off
python -m PyInstaller --onefile --add-data="../images;images" --windowed .\main.py
pause
pause