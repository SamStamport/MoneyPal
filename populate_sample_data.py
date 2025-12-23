"""
Sample Bank Account Data Generator
Run this script to populate your database with 3 months of sample data
"""

from datetime import datetime, date
from app import app
from models import db, CashFlow, ACCOUNT_TYPE_BANK

# Sample data for 3 months (September, October, November 2025)
sample_transactions = [
    # November 2025
    ('2025-11-30', -1450.00, 'Altura Heights', 'Rent payment'),
    ('2025-11-29', -850.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-11-29', 1200.00, 'John Hancock - Enron', 'Pension deposit'),
    ('2025-11-29', 950.00, 'EDS (HP) Pension', 'Pension deposit'),
    ('2025-11-29', -20.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-28', -45.50, 'Fragrancebuddy.com', 'Online purchase'),
    ('2025-11-26', -125.00, 'Farmer\'s Insurance', 'Insurance payment'),
    ('2025-11-25', -400.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-11-21', -40.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-21', -165.00, 'Green Mountain Energy', 'Electric bill'),
    ('2025-11-17', -32.75, 'Aliexpress.com', 'Online purchase'),
    ('2025-11-17', -60.00, 'Cash', 'ATM withdrawal'),
    ('2025-11-15', -750.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-11-14', -20.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-14', -45.25, 'Target', 'Groceries'),
    ('2025-11-14', -28.50, 'Target', 'Household items'),
    ('2025-11-13', -30.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-12', -25.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-12', -500.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-11-12', -40.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-11', -20.00, 'Erick', 'Cash withdrawal'),
    ('2025-11-11', 1850.00, 'Social Security', 'SS benefit deposit'),
    ('2025-11-07', 125.00, 'Fraud refund', 'Dispute resolution'),
    ('2025-11-06', -80.00, 'Cash', 'ATM withdrawal'),
    ('2025-11-05', -40.00, 'Cash', 'ATM withdrawal'),
    ('2025-11-04', -95.00, 'AT&T', 'Phone bill'),
    ('2025-11-03', -18.75, 'Schlotzskys', 'Dining'),
    ('2025-11-02', -65.50, 'HEB', 'Groceries'),
    ('2025-11-02', -22.50, 'James Coney Island', 'Dining'),
    ('2025-11-02', -1450.00, 'Altura Heights', 'Rent payment'),
    ('2025-11-01', -50.00, 'Cash', 'ATM withdrawal'),
    ('2025-11-01', -38.25, 'Target', 'Shopping'),
    ('2025-11-01', 1200.00, 'John Hancock - Enron', 'Pension deposit'),
    ('2025-11-01', 950.00, 'EDS (HP) Pension', 'Pension deposit'),
    
    # October 2025
    ('2025-10-31', -1450.00, 'Altura Heights', 'Rent payment'),
    ('2025-10-30', -800.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-10-29', 1200.00, 'John Hancock - Enron', 'Pension deposit'),
    ('2025-10-29', 950.00, 'EDS (HP) Pension', 'Pension deposit'),
    ('2025-10-28', -30.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-27', -55.25, 'HEB', 'Groceries'),
    ('2025-10-26', -125.00, 'Farmer\'s Insurance', 'Insurance payment'),
    ('2025-10-25', -450.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-10-24', -25.50, 'Whataburger', 'Dining'),
    ('2025-10-23', -40.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-22', -72.30, 'Target', 'Household items'),
    ('2025-10-21', -158.00, 'Green Mountain Energy', 'Electric bill'),
    ('2025-10-20', -20.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-19', -85.00, 'Walgreens', 'Pharmacy'),
    ('2025-10-18', -60.00, 'Cash', 'ATM withdrawal'),
    ('2025-10-17', -42.75, 'Amazon', 'Online purchase'),
    ('2025-10-16', -700.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-10-15', -30.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-14', -68.50, 'HEB', 'Groceries'),
    ('2025-10-13', -25.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-12', -35.00, 'Shell', 'Gas'),
    ('2025-10-11', -20.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-11', 1850.00, 'Social Security', 'SS benefit deposit'),
    ('2025-10-10', -550.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-10-09', -48.25, 'Target', 'Shopping'),
    ('2025-10-08', -40.00, 'Erick', 'Cash withdrawal'),
    ('2025-10-07', -32.50, 'Panda Express', 'Dining'),
    ('2025-10-06', -75.00, 'Cash', 'ATM withdrawal'),
    ('2025-10-05', -28.75, 'Walmart', 'Shopping'),
    ('2025-10-04', -95.00, 'AT&T', 'Phone bill'),
    ('2025-10-03', -52.30, 'HEB', 'Groceries'),
    ('2025-10-02', -1450.00, 'Altura Heights', 'Rent payment'),
    ('2025-10-01', 1200.00, 'John Hancock - Enron', 'Pension deposit'),
    ('2025-10-01', 950.00, 'EDS (HP) Pension', 'Pension deposit'),
    ('2025-10-01', -40.00, 'Cash', 'ATM withdrawal'),
    
    # September 2025
    ('2025-09-30', -1450.00, 'Altura Heights', 'Rent payment'),
    ('2025-09-29', -875.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-09-28', 1200.00, 'John Hancock - Enron', 'Pension deposit'),
    ('2025-09-28', 950.00, 'EDS (HP) Pension', 'Pension deposit'),
    ('2025-09-27', -35.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-26', -125.00, 'Farmer\'s Insurance', 'Insurance payment'),
    ('2025-09-25', -62.50, 'HEB', 'Groceries'),
    ('2025-09-24', -425.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-09-23', -45.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-22', -38.75, 'Chipotle', 'Dining'),
    ('2025-09-21', -142.00, 'Green Mountain Energy', 'Electric bill'),
    ('2025-09-20', -25.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-19', -55.25, 'CVS', 'Pharmacy'),
    ('2025-09-18', -70.00, 'Cash', 'ATM withdrawal'),
    ('2025-09-17', -48.50, 'Amazon', 'Online purchase'),
    ('2025-09-16', -650.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-09-15', -30.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-14', -78.25, 'Target', 'Groceries'),
    ('2025-09-13', -40.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-12', -32.50, 'Starbucks', 'Coffee'),
    ('2025-09-11', -25.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-11', 1850.00, 'Social Security', 'SS benefit deposit'),
    ('2025-09-10', -600.00, 'Capital One Master Card', 'Credit card payment'),
    ('2025-09-09', -52.75, 'HEB', 'Groceries'),
    ('2025-09-08', -35.00, 'Erick', 'Cash withdrawal'),
    ('2025-09-07', -28.50, 'Subway', 'Dining'),
    ('2025-09-06', -60.00, 'Cash', 'ATM withdrawal'),
    ('2025-09-05', -42.25, 'Walmart', 'Shopping'),
    ('2025-09-04', -95.00, 'AT&T', 'Phone bill'),
    ('2025-09-03', -68.50, 'HEB', 'Groceries'),
    ('2025-09-02', -1450.00, 'Altura Heights', 'Rent payment'),
    ('2025-09-01', 1200.00, 'John Hancock - Enron', 'Pension deposit'),
    ('2025-09-01', 950.00, 'EDS (HP) Pension', 'Pension deposit'),
    ('2025-09-01', -50.00, 'Cash', 'ATM withdrawal'),
]

def populate_sample_data():
    """Populate database with sample bank transactions"""
    with app.app_context():
        # Check if data already exists
        existing_count = CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_BANK).count()
        if existing_count > 0:
            print(f"\n⚠️  Found {existing_count} existing bank transactions.")
            response = input("Do you want to DELETE ALL existing bank data and add sample data? (yes/no): ")
            if response.lower() != 'yes':
                print("❌ Operation cancelled.")
                return
            
            # Delete existing bank data
            CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_BANK).delete()
            db.session.commit()
            print("🗑️  Deleted all existing bank transactions.")
        
        # Add sample transactions
        print("\n📊 Adding sample bank transactions...")
        for date_str, amount, description, notes in sample_transactions:
            transaction_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            entry = CashFlow(
                date=transaction_date,
                amount=amount,
                description=description,
                notes=notes,
                account_type=ACCOUNT_TYPE_BANK
            )
            db.session.add(entry)
        
        db.session.commit()
        print(f"✅ Successfully added {len(sample_transactions)} sample bank transactions!")
        print("\n📅 Date range: September 1, 2025 - November 30, 2025")
        
        # Calculate summary
        total_income = sum(amt for _, amt, _, _ in sample_transactions if amt > 0)
        total_expenses = sum(amt for _, amt, _, _ in sample_transactions if amt < 0)
        net = total_income + total_expenses
        
        print(f"\n💰 Summary:")
        print(f"   Total Income:   ${total_income:,.2f}")
        print(f"   Total Expenses: ${total_expenses:,.2f}")
        print(f"   Net Change:     ${net:,.2f}")

if __name__ == '__main__':
    populate_sample_data()