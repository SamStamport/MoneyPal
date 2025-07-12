from .auth import auth_bp
from .transactions import transactions_bp
from .dashboard import dashboard_bp
from .categories import bp as categories_bp

__all__ = ['auth_bp', 'transactions_bp', 'dashboard_bp', 'categories_bp']
