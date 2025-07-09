from flask import Blueprint, request, jsonify, render_template
from flask_login import login_user, logout_user, login_required
from models.user import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"success": True, "message": "Successfully logged in"}), 200
    
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"success": False, "message": "Email already registered"}), 400
    
    user = User(
        email=data['email'],
        password=data['password'],
        name=data['name']
    )
    user.save()
    
    return jsonify({"success": True, "message": "Successfully registered"}), 201

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"success": True, "message": "Successfully logged out"}), 200
