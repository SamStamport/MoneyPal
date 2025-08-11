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

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Main app: http://localhost:5000
   - Ideas capture: http://localhost:5000/ideas

## 📊 Usage

### Cash Flow Management
- Add income and expense entries
- Categorize transactions
- View financial summaries
- Export data for analysis

### Ideas Capture
- Quick note taking while working
- Organize thoughts by project
- Export ideas to CSV
- Perfect for project management

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

### Phase 2: Financial Features 🚧
- [ ] Complete cash flow CRUD operations
- [ ] Financial dashboard and reporting
- [ ] Category management
- [ ] Data visualization

### Phase 3: Advanced Features 📋
- [ ] User authentication
- [ ] Budget planning
- [ ] Goal tracking
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
