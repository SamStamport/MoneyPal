# Changelog

All notable changes to MoneyPal will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Complete cash flow CRUD operations (create, read, update, delete)
- Financial dashboard with monthly summaries and category breakdowns
- Sample data generation script for testing
- Project files overview documentation
- Database storage in Documents folder for persistence

### Changed
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

## [1.0.0] - 2025-09-18

### Added
- Complete financial dashboard with monthly summaries
- Full CRUD operations for cash flow transactions
- CSV export functionality for financial data
- Sample data generation for testing
- Comprehensive project documentation

### Changed
- Focused application on financial tracking only
- Database location moved to Documents folder
- Simplified project structure

### Fixed
- Database consistency across different execution methods
- Error handling for empty transaction datasets

### Removed
- Ideas capture functionality (moved to separate project)
- Desktop application features

## [0.1.0] - 2025-07-27

### Added
- Initial MoneyPal project setup
- Basic Flask application structure
- SQLAlchemy database models for cash flow tracking
- Ideas capture system with JSON export
- HTML templates for user interface
- Project configuration and dependencies

### Changed
- N/A

### Fixed
- N/A

### Removed
- N/A

## Format

### Added
- New features or functionality

### Changed
- Changes to existing functionality

### Deprecated
- Features to be removed in future releases

### Removed
- Features that have been removed

### Fixed
- Bug fixes

### Security
- Security-related fixes

[Unreleased]: https://github.com/SamStamport/MoneyPal/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/SamStamport/MoneyPal/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/SamStamport/MoneyPal/releases/tag/v0.1.0
