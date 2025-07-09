from flask import Blueprint, request, jsonify
from flask_login import login_required
from models.transaction import Transaction
from models.category import Category

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['GET'])
@login_required
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions])

@transactions_bp.route('/transactions', methods=['POST'])
@login_required
def create_transaction():
    data = request.get_json()
    
    transaction = Transaction(
        amount=data['amount'],
        description=data['description'],
        category_id=data['category_id'],
        date=data['date']
    )
    transaction.save()
    
    return jsonify(transaction.to_dict()), 201

@transactions_bp.route('/transactions/<int:id>', methods=['PUT'])
@login_required
def update_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    data = request.get_json()
    
    transaction.update(**data)
    return jsonify(transaction.to_dict())

@transactions_bp.route('/transactions/<int:id>', methods=['DELETE'])
@login_required
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    transaction.delete()
    
    return jsonify({"success": True, "message": "Transaction deleted"})

@transactions_bp.route('/categories', methods=['GET'])
@login_required
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])
