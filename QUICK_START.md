# MoneyPal Quick Start Guide

## 🚀 Start Testing in 3 Steps

### 1. Install Dependencies (run only once)
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

Tip: It's recommended to create and use a virtual environment before installing dependencies:

```powershell
python -m venv .venv
# PowerShell (Windows)
& .\.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate
```

### 3. Open in Browser
Navigate to: **http://127.0.0.1:5000/**

---

## 🧪 Database Mode Selection
- First run prompts for LIVE or SAMPLE mode
- LIVE: Real financial data (cashflowlive.db)
- SAMPLE: Test data (cashflowtest.db)
- Switch modes using "Switch DB" button

## ✨ Key Features to Test
- **Date Format**: Enter dates as mm/dd/yyyy
- **Dual Accounts**: Bank Account and Secured Visa tracking
- **Inline Editing**: Click any cell to edit and auto-save
- **Add Transactions**: Use the bottom input row + Enter key
- **AI Charts**: Visit `/charts` for forecasting visualizations
- **Export Data**: Click "Export CSV" button

---
*Ready in under 30 seconds!*