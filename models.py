from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Account type constants
ACCOUNT_TYPE_BANK = 'bank'
ACCOUNT_TYPE_SECURED_VISA = 'secured_visa'

class CashFlow(db.Model):
    __tablename__ = 'cashflow'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    notes = db.Column(db.Text)
    account_type = db.Column(db.String(50), nullable=False, default=ACCOUNT_TYPE_BANK)
    
    def __repr__(self):
        return f'<CashFlow {self.id}: {self.date} - {self.amount} - {self.account_type}>'