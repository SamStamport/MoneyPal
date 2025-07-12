from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from models.category import Category
from database import db

# Create categories blueprint
bp = Blueprint('categories', __name__)

@bp.route('/categories', methods=['GET'])
@login_required
def list_categories():
    """List all categories"""
    categories = Category.query.all()
    return render_template('categories/list.html', categories=categories)

@bp.route('/categories/new', methods=['GET', 'POST'])
@login_required
def new_category():
    """Create a new category"""
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        if not name:
            return jsonify({'error': 'Name is required'}), 400
            
        category = Category(name=name, description=description)
        category.save()
        
        return jsonify({'message': 'Category created successfully', 'category': category.to_dict()}), 201
    
    return render_template('categories/new.html')

@bp.route('/categories/<int:category_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def category(category_id):
    """Get, update, or delete a category"""
    category = Category.query.get_or_404(category_id)
    
    if request.method == 'PUT':
        data = request.get_json()
        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)
        category.save()
        return jsonify({'message': 'Category updated successfully', 'category': category.to_dict()})
    
    if request.method == 'DELETE':
        category.delete()
        return jsonify({'message': 'Category deleted successfully'})
    
    return jsonify(category.to_dict())
