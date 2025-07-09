# Development Guide

This document provides information for developers working on the MoneyPal project.

## Project Structure

```
MoneyPal/
├── app.py                # Main application entry point
├── models/              # Database models
│   ├── __init__.py
│   ├── user.py
│   └── transaction.py
├── routes/              # Application routes
│   ├── __init__.py
│   ├── auth.py
│   └── transactions.py
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
└── templates/           # HTML templates
    ├── base.html
    └── dashboard.html
```

## Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values as needed

## Database Migrations

When making changes to the database models:

1. Generate a migration:
   ```bash
   flask db migrate -m "description of changes"
   ```

2. Apply the migration:
   ```bash
   flask db upgrade
   ```

## Running Tests

Run the test suite with:
```bash
pytest
```

## Code Style

We use the following tools to maintain code quality:
- Black for code formatting
- Flake8 for linting
- Mypy for type checking

Run these tools before committing:
```bash
black .
flake8
mypy .
```

## Documentation

- Update the relevant documentation when making changes
- Keep docstrings up to date
- Document any new environment variables in `.env.example`

## Pull Requests

- Keep PRs focused on a single feature or bugfix
- Include tests for new features
- Update documentation as needed
- Reference any related issues
