from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///instance/moneypal.db')
db = SQLAlchemy(app)

# Import models after app is created
from models.user import User
from models.category import Category
from models.transaction import Transaction

print("\n=== Database Verification Script ===")
print(f"Database URI: {os.getenv('DATABASE_URL', 'sqlite:///instance/moneypal.db')}")

# Try to connect to the database
def verify_connection():
    print("\nVerifying database connection...")
    try:
        # Create a test table if it doesn't exist
        db.create_all()
        print("✅ Database connection successful!")
        
        # Check if tables exist
        print("\nChecking database tables:")
        tables = db.engine.table_names()
        for table in tables:
            print(f"- {table}")
        
        # Show table counts
        print("\nTable record counts:")
        print(f"Users: {User.query.count()}")
        print(f"Categories: {Category.query.count()}")
        print(f"Transactions: {Transaction.query.count()}")
        
        # Show sample data if exists
        print("\nSample data:")
        if User.query.count() > 0:
            print("\nFirst user:")
            user = User.query.first()
            print(f"- ID: {user.id}")
            print(f"- Email: {user.email}")
            print(f"- Name: {user.name}")
        
        if Category.query.count() > 0:
            print("\nFirst category:")
            category = Category.query.first()
            print(f"- ID: {category.id}")
            print(f"- Name: {category.name}")
            print(f"- Description: {category.description}")
        
    except Exception as e:
        print(f"❌ Error connecting to database: {str(e)}")

if __name__ == '__main__':
    with app.app_context():
        verify_connection()
