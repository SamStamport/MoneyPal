#!/usr/bin/env python3
"""
Build MoneyPal as standalone Windows executable
"""

import os
import sys

def build_executable():
    """Build standalone .exe using PyInstaller"""
    
    # Install PyInstaller if not present
    os.system("pip install pyinstaller")
    
    # Build command
    build_cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=MoneyPal",
        "--add-data=templates;templates",
        "--add-data=static;static", 
        "--add-data=models.py;.",
        "--add-data=ideas_capture.py;.",
        "--hidden-import=flask",
        "--hidden-import=flask_sqlalchemy",
        "--hidden-import=sqlalchemy",
        "--hidden-import=webview",
        "moneypal_desktop.py"
    ]
    
    print("Building MoneyPal.exe...")
    print("This may take a few minutes...")
    
    result = os.system(" ".join(build_cmd))
    
    if result == 0:
        print("\n✅ Build successful!")
        print("📁 MoneyPal.exe created in 'dist' folder")
        print("🚀 You can now run MoneyPal.exe without Python installed")
    else:
        print("\n❌ Build failed")
        print("Check error messages above")

if __name__ == "__main__":
    build_executable()