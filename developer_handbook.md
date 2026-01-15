# MoneyPal Developer Handbook

## Overview
Development guide for the MoneyPal personal finance application.

## Current Architecture

### Technology Stack
- **Backend**: Flask 3.0.0 with SQLAlchemy 1.4.53
- **Python**: Python 3.8+ recommended (virtualenv / venv for isolation)
- **Database**: SQLite with dual-mode support (LIVE/SAMPLE)
- **AI/ML**: Prophet for time series forecasting
- **Frontend**: HTML5, CSS3, JavaScript, Plotly.js

### Database Schema
```sql
CREATE TABLE cashflow (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    amount FLOAT NOT NULL,
    description VARCHAR(255),
    notes TEXT,
    account_type TEXT DEFAULT 'bank'
);
```

### Account Types
- `bank`: Bank Account transactions
- `secured_visa`: Secured Visa transactions

## Date Format Standards
- **User Input**: mm/dd/yyyy format
- **Database Storage**: ISO format (YYYY-MM-DD)
- **Display**: mm/dd/yyyy format
- **CSV Export**: mm/dd/yyyy format

Note: The application also accepts ISO `YYYY-MM-DD` input; the UI and CSV export prefer `mm/dd/yyyy` for consistency.

## Database Modes
- **LIVE**: `cashflowlive.db` - Real financial data
- **SAMPLE**: `cashflowtest.db` - Test data
- **Preference**: Stored in `db_preference.txt`

## Key Routes
- `/` - Redirects to bank account view
- `/cashflow` - Bank account management
- `/secured-visa` - Secured Visa management
- `/charts` - AI forecasting charts
- `/export-csv` - Data export

## Development Workflow

### Git Commands
```bash
git add .
git commit -m "message"
git push origin master
```

### Testing
1. Use SAMPLE mode for development
2. Test date input validation
3. Verify dual account functionality
4. Check AI forecasting with sufficient data

## Troubleshooting

### SQLAlchemy Issues
- Use SQLAlchemy 1.4.53 with Flask-SQLAlchemy 3.0.5
- Avoid SQLAlchemy 2.x for Python 3.13 compatibility
 - If using newer Python versions, verify compatibility of `sqlalchemy` and `Flask-SQLAlchemy` packages; pin versions in `requirements.txt` as needed.

### Date Format Errors
- Run `fix_date_format.py` to clean corrupted dates
- Ensure consistent mm/dd/yyyy input validation

### Unicode Issues
- Avoid emoji characters in Windows console output
- Use plain text indicators: [LIVE]/[SAMPLE]