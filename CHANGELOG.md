# Changelog

All notable changes to MoneyPal will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-01-XX

### Added
- **AI-Powered Cash Flow Forecasting**: Prophet-based time series analysis for 30-day predictions
- **Database Mode Switching**: Seamless toggle between LIVE and SAMPLE data modes
  - First-time setup prompts for database mode selection
  - Visual indicators (🔴 LIVE / 🟢 SAMPLE) in terminal and web interface
  - "Switch DB" button in all page headers
  - Persistent mode preference storage in `db_preference.txt`
- **Interactive Charts**: Plotly-based visualizations with historical data and projections
  - Combined cash flow chart with 30-day forecasting
  - Accuracy metrics display for prediction confidence
  - Hover tooltips with exact values and dates
  - Cohesive color scheme matching application design
- **Dual Account Support**: Separate tracking for Bank Account and Secured Visa
  - Individual running balance calculations
  - Account-specific data export
  - Dedicated management interfaces
- **Advanced UI Improvements**:
  - Sticky table headers that remain visible while scrolling
  - Cohesive light green color scheme across all interfaces
  - Bold axis labels in charts for better readability
  - Responsive design with consistent styling

### Changed
- **Technology Stack Enhancement**: Added pandas and prophet dependencies
- **Database Architecture**: Split into `cashflowlive.db` (real data) and `cashflowtest.db` (sample data)
- **Forecasting Logic**: Intelligent fallback from Prophet AI to simple averaging based on data availability
- **User Experience**: Prominent database mode indicators prevent accidental data mixing
- **Navigation**: Added Charts page to main navigation across all templates
 - **Charts UI**: Replaced vertical dotted date markers with a custom horizontal double-thumb slider and mini controls; added keyboard accessibility, live `mm/dd/yyyy` tooltips, a `Lock` button, and persisted selection in `localStorage` (2026-01-15).

### Fixed
- Unicode character encoding issues in Windows terminal output
- Chart toolbar styling and functionality
- Database path consistency across different execution environments
- Color scheme consistency across all application interfaces

### Technical Improvements
- Prophet integration with error handling and graceful fallbacks
- Pandas data processing for time series analysis
- Plotly.js integration for interactive visualizations
- Enhanced database configuration system
- Improved error handling and user feedback

## [1.0.0] - 2025-09-18

### Added
- **Advanced Auto-Save Functionality**: Google Sheets-like inline editing experience
  - Click any cell to edit inline with automatic saving on blur
  - Visual feedback with color-coded states (unsaved, saving, saved, error)
  - Debounced auto-save with 500ms delay to prevent excessive API calls
  - Retry logic with exponential backoff for network errors (up to 3 attempts)
  - Real-time data validation for dates and amounts
  - Error tooltips with click-to-retry functionality
  - Currency formatting for amount fields
  - ESC key to cancel editing and revert changes
  - Network status indicator (online/offline)
- **Cashflow-First Interface**: Root URL redirects to transaction management page
- Complete cash flow CRUD operations (create, read, update, delete)
- Financial dashboard with monthly summaries and category breakdowns
- Sample data generation script for testing
- Project files overview documentation
- Database storage in Documents folder for persistence

### Changed
- **Project Vision**: Evolved from traditional expense tracking to cash flow forecasting PWA
- **Interface Focus**: Cashflow page as primary interface instead of dashboard
- Removed ideas capture functionality to focus on financial tracking
- Updated database path to use Documents folder
- Streamlined project structure
- Updated documentation to reflect current features

### Fixed
- Database path consistency between different execution methods
- Monthly summary handling for empty datasets

### Removed
- Ideas capture system (moved to separate Coda integration project)
- Desktop application functionality
- Unused template files

## [0.1.0] - 2025-07-27

### Added
- Initial MoneyPal project setup
- Basic Flask application structure
- SQLAlchemy database models for cash flow tracking
- Ideas capture system with JSON export
- HTML templates for user interface
- Project configuration and dependencies

[2.0.0]: https://github.com/SamStamport/MoneyPal/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/SamStamport/MoneyPal/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/SamStamport/MoneyPal/releases/tag/v0.1.0