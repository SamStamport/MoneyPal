"""
Sample Secured Visa Card Data Generator
Run this script to populate your database with 3 months of sample data for secured card
"""

from datetime import datetime, date
from app import app
from models import db, CashFlow, ACCOUNT_TYPE_SECURED_VISA

# Sample data for 3 months (September, October, November 2025)
# This is a secured card used for everyday expenses only
# Payments are positive, purchases are negative
sample_transactions = [
    # November 2025
    ('2025-11-30', -15.75, 'McDonald\'s', 'Breakfast'),
    ('2025-11-29', -32.50, 'Shell Gas Station', 'Fuel'),
    ('2025-11-28', -8.50, 'Starbucks', 'Coffee'),
    ('2025-11-27', -45.30, 'Walmart', 'Groceries'),
    ('2025-11-26', -12.99, 'Netflix', 'Subscription'),
    ('2025-11-25', 150.00, 'Payment', 'Card payment from bank'),
    ('2025-11-24', -28.75, 'Taco Bell', 'Dinner'),
    ('2025-11-23', -55.20, 'HEB', 'Groceries'),
    ('2025-11-22', -18.50, 'Subway', 'Lunch'),
    ('2025-11-21', -35.00, 'Chevron', 'Gas'),
    ('2025-11-20', -42.35, 'Target', 'Household items'),
    ('2025-11-19', -9.99, 'Spotify', 'Subscription'),
    ('2025-11-18', -24.50, 'Chipotle', 'Lunch'),
    ('2025-11-17', -38.75, 'HEB', 'Groceries'),
    ('2025-11-16', -15.25, 'Wendy\'s', 'Lunch'),
    ('2025-11-15', 100.00, 'Payment', 'Card payment from bank'),
    ('2025-11-14', -52.80, 'Kroger', 'Groceries'),
    ('2025-11-13', -22.50, 'Pizza Hut', 'Dinner'),
    ('2025-11-12', -30.00, 'Shell Gas Station', 'Fuel'),
    ('2025-11-11', -48.25, 'Walmart', 'Shopping'),
    ('2025-11-10', -14.75, 'Dunkin Donuts', 'Coffee & snack'),
    ('2025-11-09', -36.50, 'HEB', 'Groceries'),
    ('2025-11-08', -19.99, 'Dollar General', 'Household'),
    ('2025-11-07', -28.00, 'Panda Express', 'Dinner'),
    ('2025-11-06', -33.50, 'Texaco', 'Gas'),
    ('2025-11-05', 125.00, 'Payment', 'Card payment from bank'),
    ('2025-11-04', -41.75, 'Target', 'Groceries'),
    ('2025-11-03', -16.50, 'Sonic', 'Lunch'),
    ('2025-11-02', -25.30, 'CVS', 'Pharmacy'),
    ('2025-11-01', -44.85, 'HEB', 'Groceries'),
    
    # October 2025
    ('2025-10-31', -18.50, 'Jack in the Box', 'Dinner'),
    ('2025-10-30', -35.75, 'Shell Gas Station', 'Fuel'),
    ('2025-10-29', -9.25, 'Starbucks', 'Coffee'),
    ('2025-10-28', -48.60, 'Walmart', 'Groceries'),
    ('2025-10-27', -22.00, 'Whataburger', 'Lunch'),
    ('2025-10-26', -12.99, 'Hulu', 'Subscription'),
    ('2025-10-25', 150.00, 'Payment', 'Card payment from bank'),
    ('2025-10-24', -31.50, 'Chili\'s', 'Dinner'),
    ('2025-10-23', -52.30, 'HEB', 'Groceries'),
    ('2025-10-22', -16.75, 'Taco Cabana', 'Lunch'),
    ('2025-10-21', -38.00, 'Chevron', 'Gas'),
    ('2025-10-20', -45.20, 'Target', 'Shopping'),
    ('2025-10-19', -11.50, 'McDonald\'s', 'Breakfast'),
    ('2025-10-18', -28.75, 'Panera Bread', 'Lunch'),
    ('2025-10-17', -42.85, 'HEB', 'Groceries'),
    ('2025-10-16', -19.25, 'Five Guys', 'Dinner'),
    ('2025-10-15', 125.00, 'Payment', 'Card payment from bank'),
    ('2025-10-14', -55.40, 'Kroger', 'Groceries'),
    ('2025-10-13', -24.50, 'Olive Garden', 'Dinner'),
    ('2025-10-12', -32.00, 'Shell Gas Station', 'Fuel'),
    ('2025-10-11', -46.75, 'Walmart', 'Shopping'),
    ('2025-10-10', -13.99, 'Dairy Queen', 'Dessert'),
    ('2025-10-09', -39.50, 'HEB', 'Groceries'),
    ('2025-10-08', -21.25, 'Dollar Tree', 'Household'),
    ('2025-10-07', -26.00, 'Chipotle', 'Dinner'),
    ('2025-10-06', -34.75, 'Texaco', 'Gas'),
    ('2025-10-05', 100.00, 'Payment', 'Card payment from bank'),
    ('2025-10-04', -43.60, 'Target', 'Groceries'),
    ('2025-10-03', -17.50, 'Subway', 'Lunch'),
    ('2025-10-02', -29.85, 'Walgreens', 'Pharmacy'),
    ('2025-10-01', -47.25, 'HEB', 'Groceries'),
    
    # September 2025
    ('2025-09-30', -20.00, 'Burger King', 'Dinner'),
    ('2025-09-29', -36.50, 'Shell Gas Station', 'Fuel'),
    ('2025-09-28', -10.25, 'Starbucks', 'Coffee'),
    ('2025-09-27', -51.30, 'Walmart', 'Groceries'),
    ('2025-09-26', -23.75, 'Popeyes', 'Lunch'),
    ('2025-09-25', 150.00, 'Payment', 'Card payment from bank'),
    ('2025-09-24', -33.50, 'Red Lobster', 'Dinner'),
    ('2025-09-23', -49.80, 'HEB', 'Groceries'),
    ('2025-09-22', -18.25, 'Jimmy John\'s', 'Lunch'),
    ('2025-09-21', -37.00, 'Chevron', 'Gas'),
    ('2025-09-20', -44.60, 'Target', 'Shopping'),
    ('2025-09-19', -12.99, 'Amazon Prime', 'Subscription'),
    ('2025-09-18', -27.50, 'Applebee\'s', 'Dinner'),
    ('2025-09-17', -41.75, 'HEB', 'Groceries'),
    ('2025-09-16', -16.00, 'Arby\'s', 'Lunch'),
    ('2025-09-15', 125.00, 'Payment', 'Card payment from bank'),
    ('2025-09-14', -53.20, 'Kroger', 'Groceries'),
    ('2025-09-13', -25.75, 'Buffalo Wild Wings', 'Dinner'),
    ('2025-09-12', -31.50, 'Shell Gas Station', 'Fuel'),
    ('2025-09-11', -48.35, 'Walmart', 'Shopping'),
    ('2025-09-10', -14.25, 'Sonic', 'Lunch'),
    ('2025-09-09', -38.90, 'HEB', 'Groceries'),
    ('2025-09-08', -22.50, 'Family Dollar', 'Household'),
    ('2025-09-07', -29.00, 'Panda Express', 'Dinner'),
    ('2025-09-06', -35.25, 'Texaco', 'Gas'),
    ('2025-09-05', 100.00, 'Payment', 'Card payment from bank'),
    ('2025-09-04', -42.45, 'Target', 'Groceries'),
    ('2025-09-03', -19.75, 'Taco Bell', 'Lunch'),
    ('2025-09-02', -28.50, 'CVS', 'Pharmacy'),
    ('2025-09-01', 200.00, 'Payment', 'Initial card deposit'),
    ('2025-09-01', -46.60, 'HEB', 'Groceries'),
]

def populate_secured_visa_data():
    """Populate database with sample secured visa transactions"""
    with app.app_context():
        # Check if data already exists
        existing_count = CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_SECURED_VISA).count()
        if existing_count > 0:
            print(f"\n⚠️  Found {existing_count} existing secured visa transactions.")
            response = input("Do you want to DELETE ALL existing secured visa data and add sample data? (yes/no): ")
            if response.lower() != 'yes':
                print("❌ Operation cancelled.")
                return
            
            # Delete existing secured visa data
            CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_SECURED_VISA).delete()
            db.session.commit()
            print("🗑️  Deleted all existing secured visa transactions.")
        
        # Add sample transactions
        print("\n💳 Adding sample secured visa transactions...")
        for date_str, amount, description, notes in sample_transactions:
            transaction_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            entry = CashFlow(
                date=transaction_date,
                amount=amount,
                description=description,
                notes=notes,
                account_type=ACCOUNT_TYPE_SECURED_VISA
            )
            db.session.add(entry)
        
        db.session.commit()
        print(f"✅ Successfully added {len(sample_transactions)} sample secured visa transactions!")
        print("\n📅 Date range: September 1, 2025 - November 30, 2025")
        
        # Calculate summary
        total_payments = sum(amt for _, amt, _, _ in sample_transactions if amt > 0)
        total_purchases = sum(amt for _, amt, _, _ in sample_transactions if amt < 0)
        net = total_payments + total_purchases
        
        print(f"\n💰 Summary:")
        print(f"   Total Payments:  ${total_payments:,.2f}")
        print(f"   Total Purchases: ${total_purchases:,.2f}")
        print(f"   Net Balance:     ${net:,.2f}")
        print(f"\n📊 Transaction breakdown:")
        print(f"   Groceries (HEB, Walmart, Target, Kroger): ~{sum(1 for _, _, d, _ in sample_transactions if any(store in d for store in ['HEB', 'Walmart', 'Target', 'Kroger']))}")
        print(f"   Gas (Shell, Chevron, Texaco): ~{sum(1 for _, _, d, _ in sample_transactions if any(gas in d for gas in ['Shell', 'Chevron', 'Texaco', 'Gas']))}")
        print(f"   Dining/Fast Food: ~{sum(1 for _, _, d, _ in sample_transactions if any(rest in d for rest in ['McDonald', 'Taco', 'Subway', 'Pizza', 'Chipotle', 'Starbucks', 'Wendy', 'Burger', 'Sonic']))}")
        print(f"   Subscriptions: ~{sum(1 for _, _, d, _ in sample_transactions if any(sub in d for sub in ['Netflix', 'Spotify', 'Hulu', 'Prime']))}")

if __name__ == '__main__':
    populate_secured_visa_data()