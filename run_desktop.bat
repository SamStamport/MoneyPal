@echo off
cd /d "C:\Users\samst\VS Code projects\MoneyPal"
echo Installing desktop requirements...
pip install -r requirements_desktop.txt
echo.
echo Starting MoneyPal Desktop App...
python moneypal_desktop.py
pause