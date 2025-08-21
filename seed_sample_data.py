from datetime import date, timedelta
import random
from flask import Flask
from models import db, CashFlow

# Configuration
DB_URI = 'sqlite:///cashflow.db'
START_DATE = date(2025, 6, 1)
END_DATE = date(2025, 7, 31)
STARTING_BALANCE = 3250.00  # Made-up starting balance

# Categories and sample descriptions
CATEGORIES = {
    'groceries': [
        'Walmart', 'Target', 'Whole Foods', 'Trader Joe\'s', 'Kroger', 'Aldi', 'Safeway'
    ],
    'restaurants': [
        'Chipotle', 'Olive Garden', 'Local Diner', 'Sushi House', 'Pizza Palace',
        'Taco Loco', 'Burger Barn', 'Thai Spice', 'Curry Corner', 'Noodle Nook'
    ],
    'miscellaneous': [
        'Amazon', 'Best Buy', 'Home Depot', 'IKEA', 'Pharmacy', 'Apple Store'
    ],
    'gas': [
        'Shell', 'Exxon', 'Chevron', 'BP', 'Costco Gas'
    ],
    'utilities': [
        'Electric Co', 'Water Co', 'Internet Provider'
    ],
    'rent': [
        'Monthly Rent'
    ],
    'deposit': [
        'Paycheck', 'Transfer In', 'Refund'
    ]
}

random.seed(42)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def pick_deposit_days_for_month(year: int, month: int, max_deposits: int = 3):
    # Choose 1 to 3 deposit days per month
    num = random.choice([1, 2, 3])
    if num > max_deposits:
        num = max_deposits
    # Pick distinct days in range 1..28 to avoid month-end edge cases
    days = random.sample(range(1, 29), num)
    return set(days)


def generate_amount(min_val: float, max_val: float, negative: bool = False) -> float:
    amt = round(random.uniform(min_val, max_val), 2)
    if negative:
        amt = -abs(amt)
    return amt


def cap_to_balance(balance: float, change: float) -> float:
    """Ensure running balance never goes negative after applying change.
    If change would make it negative, reduce magnitude for purchases or skip if zero room.
    """
    if change >= 0:
        return change
    # For purchases (negative), cap so balance stays >= 0.01
    max_spend = max(0.0, round(balance - 0.01, 2))
    spend = min(abs(change), max_spend)
    return -spend


def clear_existing_range(start: date, end: date):
    # Remove existing entries in the date range to avoid duplicates
    # Use the actual table name from the database
    db.session.execute('DELETE FROM cash_flow WHERE date >= :start AND date <= :end', 
                      {'start': start, 'end': end})
    db.session.commit()


def seed_data():
    app = create_app()
    with app.app_context():
        clear_existing_range(START_DATE, END_DATE)

        running_balance = STARTING_BALANCE

        # Insert an initial balance marker on the day before start (optional)
        initial_marker_date = START_DATE - timedelta(days=1)
        db.session.add(CashFlow(
            date=initial_marker_date,
            amount=STARTING_BALANCE,
            description='Starting Balance',
            category='starting_balance',
            notes='Auto-generated seed'
        ))

        # Plan deposit days per month
        deposit_days = {
            (2025, 6): pick_deposit_days_for_month(2025, 6, max_deposits=3),
            (2025, 7): pick_deposit_days_for_month(2025, 7, max_deposits=3),
        }

        # Add one rent transaction per month (kept within -600 cap)
        rent_amount = -600.00
        rent_days = {
            (2025, 6): random.choice([1, 2, 3, 4, 5]),
            (2025, 7): random.choice([1, 2, 3, 4, 5])
        }

        current = START_DATE
        while current <= END_DATE:
            y, m, d = current.year, current.month, current.day

            # 1) Deposits (no more than 3/month)
            if d in deposit_days.get((y, m), set()):
                # Deposit between 300 and 600
                dep = generate_amount(300, 600, negative=False)
                db.session.add(CashFlow(
                    date=current,
                    amount=dep,
                    description=random.choice(CATEGORIES['deposit']),
                    category='deposit',
                    notes='Auto-generated seed'
                ))
                running_balance = round(running_balance + dep, 2)

            # 2) Rent once per month if today is designated day
            if d == rent_days[(y, m)]:
                amt = cap_to_balance(running_balance, rent_amount)
                if amt != 0:
                    db.session.add(CashFlow(
                        date=current,
                        amount=amt,
                        description='Monthly Rent',
                        category='rent',
                        notes='Auto-generated seed'
                    ))
                    running_balance = round(running_balance + amt, 2)

            # 3) Random number of other purchases this day (0 to 3)
            num_purchases = random.choices([0, 1, 2, 3], weights=[4, 3, 2, 1])[0]
            for _ in range(num_purchases):
                cat = random.choice(['groceries', 'restaurants', 'miscellaneous', 'gas', 'utilities'])
                desc = random.choice(CATEGORIES[cat])
                spend = generate_amount(23, 180, negative=True)
                spend = cap_to_balance(running_balance, spend)
                if spend == 0:
                    continue
                db.session.add(CashFlow(
                    date=current,
                    amount=spend,
                    description=desc,
                    category=cat,
                    notes='Auto-generated seed'
                ))
                running_balance = round(running_balance + spend, 2)

            current += timedelta(days=1)

        db.session.commit()

        # Basic summary - use the actual table name
        from sqlalchemy import func
        totals = db.session.execute(
            'SELECT strftime("%Y-%m", date) as ym, COUNT(*) as count, SUM(amount) as total '
            'FROM cash_flow WHERE date >= :start AND date <= :end GROUP BY ym',
            {'start': START_DATE, 'end': END_DATE}
        ).fetchall()

        print('Seeding complete.')
        for ym, count, total in totals:
            print(f'{ym}: {count} rows, net {float(total or 0):.2f}')
        print(f'Ending balance: {running_balance:.2f}')


if __name__ == '__main__':
    seed_data()
