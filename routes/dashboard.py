from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.transaction import Transaction
from models.category import Category

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    # Get user's transactions and categories
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    categories = Category.query.all()
    
    return render_template('dashboard.html',
                         transactions=transactions,
                         categories=categories)
