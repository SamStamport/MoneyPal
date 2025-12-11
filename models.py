from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CashFlow(db.Model):
    __tablename__ = 'cashflow'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    notes = db.Column(db.Text)
    
    def __repr__(self):
        return f'<CashFlow {self.id}: {self.date} - {self.amount}>'