#!/usr/bin/env python3
"""Check if all requirements are met for MoneyPal"""

def check_requirements():
    print("Checking MoneyPal requirements for Windows...")
    print("=" * 50)
    
    # Check Python version
    import sys
    print(f"[OK] Python version: {sys.version}")
    
    # Check required packages
    required_packages = [
        ('flask', 'Flask'),
        ('flask_sqlalchemy', 'Flask-SQLAlchemy'), 
        ('sqlalchemy', 'SQLAlchemy'),
        ('datetime', 'datetime (built-in)'),
        ('json', 'json (built-in)'),
        ('os', 'os (built-in)')
    ]
    
    missing_packages = []
    
    for module_name, display_name in required_packages:
        try:
            __import__(module_name)
            print(f"[OK] {display_name}")
        except ImportError:
            print(f"[MISSING] {display_name}")
            missing_packages.append(display_name)
    
    # Check project files
    import os
    required_files = [
        'models.py',
        'ideas_capture.py', 
        'templates/dashboard.html',
        'templates/cashflow.html',
        'templates/ideas.html'
    ]
    
    print("\nChecking project files:")
    print("-" * 30)
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"[OK] {file_path}")
        else:
            print(f"[MISSING] {file_path}")
            missing_packages.append(file_path)
    
    # Test imports from project modules
    print("\nTesting project module imports:")
    print("-" * 35)
    
    try:
        import models
        print("[OK] models.py imports successfully")
    except Exception as e:
        print(f"[ERROR] models.py import failed: {e}")
        missing_packages.append("models.py import")
    
    try:
        import ideas_capture
        print("[OK] ideas_capture.py imports successfully")
    except Exception as e:
        print(f"[ERROR] ideas_capture.py import failed: {e}")
        missing_packages.append("ideas_capture.py import")
    
    # Summary
    print("\n" + "=" * 50)
    if not missing_packages:
        print("ALL REQUIREMENTS MET! MoneyPal is ready to run on Windows.")
        print("\nTo start the application:")
        print("1. python app.py")
        print("2. Open browser to http://127.0.0.1:5000")
    else:
        print("MISSING REQUIREMENTS:")
        for item in missing_packages:
            print(f"   - {item}")
        print("\nTo fix missing packages, run:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    check_requirements()