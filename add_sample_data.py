from datetime import date
from app import app, db, CashFlow

with app.app_context():
    # Clear existing data
    CashFlow.query.delete()
    
    # Add sample entries
    entries = [
        CashFlow(date=date(2025, 5, 31), amount=3250.00, description='Starting Balance', category='starting_balance', notes='Initial balance'),
        CashFlow(date=date(2025, 6, 1), amount=326.08, description='Transfer In', category='deposit', notes='Paycheck'),
        CashFlow(date=date(2025, 6, 1), amount=-600.00, description='Monthly Rent', category='rent', notes='June rent'),
        CashFlow(date=date(2025, 6, 4), amount=480.61, description='Refund', category='deposit', notes='Tax refund'),
        CashFlow(date=date(2025, 6, 5), amount=-45.23, description='Walmart', category='groceries', notes='Weekly shopping'),
        CashFlow(date=date(2025, 6, 7), amount=-32.50, description='Shell Gas', category='gas', notes='Fill up'),
    ]
    
    for entry in entries:
        db.session.add(entry)
    
    db.session.commit()
    print(f"Added {len(entries)} sample entries!")
