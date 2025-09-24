# MoneyPal - Personal Cash Flow Tracker

> **🚀 QUICK START REMINDER:** After running `python app.py`, open http://127.0.0.1:5000/ in your browser

A Flask-based personal finance PWA focused on **cash flow forecasting** rather than traditional budgeting. The key insight: most apps track past spending but don't solve the real problem of "will I have enough money left at the end of the month?"

## 💡 Project Vision

**MoneyPal** addresses a key gap in personal finance apps: most track past spending but don't solve the real problem of "will I have enough money left at the end of the month?"

### Our Approach
- **Cash Flow Forecasting**: AI-powered predictions based on historical spending patterns
- **Forward-Looking**: Focus on future financial health vs. past analysis
- **Voice-First**: Hands-free expense logging and conversational financial insights
- **Privacy-Focused**: Manual data entry gives users full control over their financial data
- **Minimal & Focused**: Essential features without bloat

### Target Users
- People frustrated with traditional budgeting apps
- Those seeking forward-looking financial insights
- Users who value privacy and data control
- Individuals wanting hands-free expense tracking

### Competitive Advantages
- **Cash flow forecasting** is rare in consumer finance apps
- **Voice-first interaction** for accessibility and convenience
- **Privacy-focused** manual entry approach
- **Minimal, focused** feature set vs. bloated competitors

## 🚀 Features

### Core Functionality
- **Cash Flow Tracking**: Record income and expenses with categories
- **Auto-Save Editing**: Click any cell to edit inline with automatic saving
- **Forward-Looking Insights**: Focus on cash flow forecasting vs. past spending analysis
- **Category Management**: Organize transactions by type and purpose
- **Data Export**: Export financial data in multiple formats



## 🛠️ Technology Stack

- **Backend**: Flask 3.0.0, Python 3.6+
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Dependencies**: Flask-SQLAlchemy, python-dotenv

## 📁 Project Structure

```
MoneyPal/
├── app.py                 # Main Flask application
├── models.py             # Database models (CashFlow)
├── requirements.txt      # Python dependencies
├── seed_sample_data.py   # Sample data generator
├── templates/            # HTML templates
│   ├── dashboard.html   # Financial dashboard
│   └── cashflow.html    # Cash flow management
└── project_files_overview.txt # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SamStamport/MoneyPal.git
   cd MoneyPal
   ```

2. **Install dependencies and run**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   Then visit: http://localhost:5000

## 📊 Usage

### Cash Flow Management
- Add income and expense entries with Enter key
- **Inline Editing**: Click any cell (date, amount, description, category, notes) to edit
- **Auto-Save**: Changes save automatically when you click away
- **Visual Feedback**: See saving status with color-coded indicators
- **Error Handling**: Automatic retry on network errors with visual feedback
- **Data Validation**: Real-time validation for dates and amounts
- Categorize transactions
- View financial dashboard with monthly summaries
- Export data to CSV format



## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///cashflow.db
```

### Database
The application uses SQLite and stores data in `C:\Users\[username]\Documents\MoneyPal\cashflow.db`. The database will be created automatically on first run.

## 📈 Roadmap

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
- [x] Financial dashboard and reporting
- [x] Category management

### Phase 3: AI-Powered Features 📋
- [ ] **AI Cash Flow Prediction**: Historical data analysis for future forecasting
- [ ] **Voice Input**: Speech recognition for hands-free expense logging
- [ ] **Receipt Photo Capture**: AI parsing of receipt images
- [ ] **Smart Alerts**: Upcoming low balance period notifications
- [ ] **Conversational Interface**: Voice queries for cash flow insights
- [ ] **Recurring Bills Integration**: Predictable expense automation

### Phase 4: Advanced Features 📋
- [ ] Data visualization charts
- [ ] Goal tracking
- [ ] User authentication
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
- **Documentation**: Check the project_files_overview.txt for detailed file descriptions
- **Questions**: Open a discussion on GitHub

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and updates.

---

**MoneyPal** - Take control of your finances, one transaction at a time.
