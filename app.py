from flask import Flask, render_template
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure secret key for Flask-Login
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///moneypal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
from database import db
db.init_app(app)

# Add root route
@app.route('/')
def index():
    return render_template('dashboard.html')

# Import routes after app is initialized
from routes import auth_bp, transactions_bp, dashboard_bp, categories_bp

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(categories_bp, url_prefix='/categories')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
