# MoneyPal - Personal Cash Flow Tracker

> **🚀 QUICK START REMINDER:** After running `python app.py`, open http://127.0.0.1:5000/ in your browser

A Flask-based personal finance PWA focused on **cash flow forecasting** rather than traditional budgeting. The key insight: most apps track past spending but don't solve the real problem of "will I have enough money left at the end of the month?"

## 💡 Project Vision

**MoneyPal** addresses a key gap in personal finance apps: most track past spending but don't solve the real problem of "will I have enough money left at the end of the month?"

### Our Approach
- **AI-Powered Cash Flow Forecasting**: Prophet-based predictions using historical spending patterns
- **Forward-Looking**: Focus on future financial health vs. past analysis
- **Database Switching**: Seamless switching between LIVE and SAMPLE data modes
- **Privacy-Focused**: Manual data entry gives users full control over their financial data
- **Minimal & Focused**: Essential features without bloat

### Target Users
- People frustrated with traditional budgeting apps
- Those seeking forward-looking financial insights
- Users who value privacy and data control
- Individuals wanting reliable cash flow predictions

### Competitive Advantages
- **AI cash flow forecasting** with Prophet time series analysis
- **Database mode switching** for safe testing and live data
- **Privacy-focused** manual entry approach
- **Minimal, focused** feature set vs. bloated competitors

## 🚀 Features

### Core Functionality ✅
- **Cash Flow Tracking**: Record income and expenses for Bank Account and Secured Visa
- **Auto-Save Editing**: Click any cell to edit inline with automatic saving
- **AI-Powered Forecasting**: 30-day cash flow predictions using Prophet or simple averaging
- **Interactive Charts**: Plotly-based visualizations with historical data and projections
- **Database Mode Switching**: Toggle between LIVE (real data) and SAMPLE (test data) modes
- **Sticky Headers**: Table headers remain visible while scrolling
- **Data Export**: Export financial data in CSV format
- **Running Balance**: Real-time balance calculations across all transactions

### Advanced Features ✅
- **Prophet AI Integration**: Advanced time series forecasting with accuracy metrics
- **Dual Account Support**: Separate tracking for Bank Account and Secured Visa
- **Visual Database Indicators**: Clear [LIVE] / [SAMPLE] mode display
- **Responsive Design**: Cohesive color scheme across all interfaces
- **Error Handling**: Graceful fallback from AI to simple forecasting

## 🛠️ Technology Stack

- **Backend**: Flask 3.0.0, Python 3.8+
- **Database**: SQLite with SQLAlchemy 1.4.53
- **AI/ML**: Prophet for time series forecasting, Pandas for data processing
- **Frontend**: HTML5, CSS3, JavaScript, Plotly.js for charts
- **Dependencies**: Flask-SQLAlchemy 3.0.5, python-dotenv, pandas, prophet

## 📁 Project Structure

```
MoneyPal/
├── app.py                          # Main Flask application with AI forecasting
├── models.py                       # Database models (CashFlow)
├── requirements.txt                # Python dependencies including Prophet
├── db_preference.txt               # Database mode preference (LIVE/SAMPLE)
├── cashflowlive.db                 # Live database (real data)
├── cashflowtest.db                 # Sample database (test data)
├── populate_sample_data.py         # Sample data generator
├── populate_secured_visa_data.py   # Secured Visa sample data
├── templates/                      # HTML templates
│   ├── cashflow.html              # Bank account management
│   ├── secured_visa.html           # Secured Visa management
│   └── charts.html                 # Interactive charts with forecasting
└── README.md                       # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SamStamport/MoneyPal.git
   cd MoneyPal
   ```

2. **Install dependencies and run**
   ```bash
   # Create and activate a virtual environment (recommended)
   python -m venv .venv
   # PowerShell (Windows)
   & .\.venv\Scripts\Activate.ps1
   # macOS / Linux
   # source .venv/bin/activate

   pip install -r requirements.txt
   python app.py
   ```
   
3. **First-time setup**
   - Choose LIVE or SAMPLE database mode when prompted
   - Visit: http://localhost:5000

## 📊 Usage

### Database Mode Selection
- **First Run**: Terminal prompts for LIVE or SAMPLE mode
- **Subsequent Runs**: Automatically uses saved preference
- **Mode Switching**: Use "Switch DB" button in any page header
- **Visual Indicators**: 🔴 LIVE DATABASE or 🟢 SAMPLE DATABASE always visible

### Cash Flow Management
- **Dual Accounts**: Separate Bank Account and Secured Visa tracking
- **Date Format**: Enter dates in mm/dd/yyyy format
- **Inline Editing**: Click any cell (date, amount, description, notes) to edit
- **Auto-Save**: Changes save automatically when you click away
- **Running Balance**: Real-time balance calculations
- **Sticky Headers**: Headers remain visible while scrolling through data

Note: The application accepts both `mm/dd/yyyy` (user-friendly) and ISO `YYYY-MM-DD` date formats. When adding or editing via the UI prefer `mm/dd/yyyy` for consistency with CSV export.

### AI-Powered Forecasting
- **Charts Page**: Interactive Plotly visualizations
- **Prophet Integration**: Advanced time series analysis for 10+ data points
- **Simple Fallback**: Average-based predictions for smaller datasets
- **Accuracy Metrics**: Confidence intervals and accuracy percentages
- **30-Day Projections**: Future balance predictions for both accounts

## 🔧 Configuration

### Database Modes
- **LIVE Mode**: Uses `cashflowlive.db` for real financial data
- **SAMPLE Mode**: Uses `cashflowtest.db` for testing and demonstrations
- **Preference Storage**: Mode saved in `db_preference.txt`
- **Safe Switching**: Clear visual indicators prevent accidental data mixing

### Environment Variables (Optional)
Create a `.env` file in the project root:
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

## 📈 Current Status

### Phase 1: Core Features ✅
- [x] Basic Flask application structure
- [x] Database models and setup
- [x] CSV export functionality
- [x] Sample data generation

### Phase 2: Financial Features ✅
- [x] Complete cash flow CRUD operations
- [x] Inline editing with auto-save functionality
- [x] Visual feedback and error handling
- [x] Data validation and currency formatting
- [x] Dual account support (Bank + Secured Visa)
- [x] Running balance calculations

### Phase 3: AI-Powered Features ✅
- [x] **AI Cash Flow Prediction**: Prophet-based forecasting with accuracy metrics
- [x] **Interactive Charts**: Plotly visualizations with historical and projected data
- [x] **Database Mode Switching**: Safe LIVE/SAMPLE data separation
- [x] **Advanced UI**: Sticky headers, cohesive color scheme
- [x] **Error Handling**: Graceful AI fallback to simple methods

### Phase 4: Advanced Features 📋
- [ ] Voice input for expense logging
- [ ] Receipt photo capture with AI parsing
- [ ] Smart alerts for low balance predictions
- [ ] Goal tracking and budget management
- [ ] User authentication system
- [ ] Mobile PWA optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs and feature requests on GitHub
- **Documentation**: Check the ROADMAP.md and CHANGELOG.md for detailed information
- **Questions**: Open a discussion on GitHub

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and updates.

---

**MoneyPal** - Take control of your finances with AI-powered forecasting.