from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from models.user import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    # Handle both JSON and form data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    
    user = User.query.filter_by(email=data['email']).first()
    
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return redirect(url_for('dashboard.index'))
    
    flash('Invalid email or password', 'error')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    # Handle both JSON and form data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    
    if User.query.filter_by(email=data['email']).first():
        flash('Email already registered', 'error')
        return redirect(url_for('auth.register'))
    
    user = User(
        email=data['email'],
        password=data['password'],
        name=data['name']
    )
    user.save()
    
    login_user(user)
    flash('Successfully registered!', 'success')
    return redirect(url_for('dashboard.index'))

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"success": True, "message": "Successfully logged out"}), 200
