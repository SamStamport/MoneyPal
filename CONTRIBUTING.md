# Contributing to MoneyPal

Thank you for considering contributing to MoneyPal! We welcome any contributions that can help improve this project.

## How to Contribute

1. **Fork** the repository and create your branch from `main`.
2. **Clone** the repository to your local machine.
3. **Create a new branch** for your feature or bugfix.
4. **Commit** your changes with descriptive commit messages.
5. **Push** your changes to your fork.
6. Open a **pull request** with a clear description of your changes.

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file (use `.env.example` as a template).

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use type hints where appropriate.
- Write docstrings for all public functions and classes.

## Testing

Please ensure all new code is covered by tests. Run the test suite with:

```bash
pytest
```

## Reporting Issues

When reporting issues, please include:
- A clear description of the problem
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any relevant error messages or screenshots

## Feature Requests

We welcome feature requests! Please open an issue to discuss your idea before starting work on it.
