# MoneyPal - Personal Cash Flow Tracker

A Flask-based web application for tracking personal income, expenses, and financial goals. Built with modern web technologies and designed for easy use and data export.

## 🚀 Features

### Core Functionality
- **Cash Flow Tracking**: Record income and expenses with categories
- **Financial Dashboard**: Visual overview of your financial health
- **Category Management**: Organize transactions by type and purpose
- **Data Export**: Export financial data in multiple formats

### Ideas Capture System
- **Quick Note Taking**: Capture thoughts, todos, and code snippets
- **CSV Export**: Export ideas to spreadsheet applications
- **Tagging System**: Organize ideas with custom tags and categories
- **Persistent Storage**: All data saved locally

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
├── ideas_capture.py      # Ideas capture system
├── requirements.txt      # Python dependencies
├── cashflow.db          # SQLite database
├── templates/            # HTML templates
│   ├── cashflow.html    # Cash flow management
│   └── ideas.html       # Ideas capture interface
└── instance/            # Instance-specific files
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

2. **Run as Desktop App (Recommended)**
   ```bash
   # Double-click run_desktop.bat or run in command prompt:
   run_desktop.bat
   ```
   This automatically installs dependencies and launches the native Windows app.

3. **Alternative: Web Browser Mode**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   Then visit: http://localhost:5000

## 📊 Usage

### Desktop Application
- **Launch**: Double-click `run_desktop.bat`
- **Interface**: Native Windows application window
- **Close**: Click the X button on the app window
- **Data**: Automatically saved to local database

### Cash Flow Management
- Add income and expense entries
- Categorize transactions
- View financial dashboard with monthly summaries
- Export data to CSV format

### Ideas Capture
- Quick note taking while working
- Organize thoughts by project
- Export ideas to CSV
- Access via /ideas route

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///cashflow.db
```

### Database
The application uses SQLite by default. The database file (`cashflow.db`) will be created automatically on first run.

## 📈 Roadmap

### Phase 1: Core Features ✅
- [x] Basic Flask application structure
- [x] Database models and setup
- [x] Ideas capture system
- [x] CSV export functionality

### Phase 2: Financial Features ✅
- [x] Complete cash flow CRUD operations
- [x] Financial dashboard and reporting
- [x] Category management
- [x] Native desktop application

### Phase 3: Advanced Features 📋
- [ ] Data visualization charts
- [ ] Budget planning and alerts
- [ ] Goal tracking
- [ ] Standalone executable (.exe)
- [ ] User authentication
- [ ] Mobile app

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
- **Documentation**: Check the [IDEAS_CAPTURE_README.md](IDEAS_CAPTURE_README.md) for detailed usage
- **Questions**: Open a discussion on GitHub

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and updates.

---

**MoneyPal** - Take control of your finances, one transaction at a time.
