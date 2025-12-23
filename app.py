from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
from models import db, CashFlow
from sqlalchemy import func
import os

app = Flask(__name__)

# Configure database URI and disable track modifications for performance
db_path = os.path.join(os.path.dirname(__file__), 'cashflow.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB tables if they don't exist yet
with app.app_context():
    db.create_all()
    print("\033[1;34m✔️ Database initialized — loading complete.\033[0m")


@app.route('/', methods=['GET'])
def index():
    from flask import redirect, url_for
    return redirect(url_for('list_entries'))


@app.route('/dashboard', methods=['GET'])
def dashboard():
    today = date.today()
    current_month = today.month
    current_year = today.year
    
    monthly_summary = db.session.query(
        func.sum(CashFlow.amount).label('total'),
        func.count(CashFlow.id).label('count')
    ).filter(
        func.extract('month', CashFlow.date) == current_month,
        func.extract('year', CashFlow.date) == current_year
    ).first()
    
    if monthly_summary.total is None:
        monthly_summary = type('obj', (object,), {'total': 0, 'count': 0})()
    
    recent_entries = CashFlow.query.order_by(CashFlow.date.desc()).limit(10).all()
    net_worth = db.session.query(func.sum(CashFlow.amount)).scalar() or 0
    
    return render_template(
        'dashboard.html',
        monthly_summary=monthly_summary,
        recent_entries=recent_entries,
        net_worth=net_worth,
        current_month=current_month,
        current_year=current_year
    )


@app.route('/cashflow', methods=['GET'])
def list_entries():
    entries = CashFlow.query.filter_by(account_type='bank').order_by(CashFlow.date.desc()).all()
    return render_template('cashflow.html', entries=entries)


@app.route('/secured-visa', methods=['GET'])
def secured_visa():
    entries = CashFlow.query.filter_by(account_type='secured_visa').order_by(CashFlow.date.desc()).all()
    return render_template('secured_visa.html', entries=entries)


@app.route('/add-ajax', methods=['POST'])
def add_entry_ajax():
    try:
        data = request.get_json()
        date_obj = datetime.strptime(data['date'], "%Y-%m-%d").date()
        amount = float(data['amount'])
        description = data.get('description', '')
        notes = data.get('notes', '')
        account_type = data.get('account_type', 'bank')

        new_entry = CashFlow(
            date=date_obj,
            amount=amount,
            description=description,
            notes=notes,
            account_type=account_type
        )
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({
            'id': new_entry.id,
            'date': new_entry.date.strftime("%Y-%m-%d"),
            'amount': new_entry.amount,
            'description': new_entry.description,
            'notes': new_entry.notes
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/update/<int:entry_id>', methods=['POST'])
def update_entry(entry_id):
    try:
        data = request.get_json()
        entry = CashFlow.query.get_or_404(entry_id)

        if 'date' in data:
            entry.date = datetime.strptime(data['date'], "%Y-%m-%d").date()
        if 'amount' in data:
            entry.amount = float(data['amount'])
        if 'description' in data:
            entry.description = data['description']
        if 'notes' in data:
            entry.notes = data['notes']

        db.session.commit()
        return jsonify({'success': True}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/delete/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    try:
        entry = CashFlow.query.get_or_404(entry_id)
        db.session.delete(entry)
        db.session.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/export-csv', methods=['GET'])
def export_cashflow_csv():
    from io import StringIO
    import csv
    
    entries = CashFlow.query.order_by(CashFlow.date).all()
    
    csvfile = StringIO()
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Amount', 'Description', 'Notes'])
    
    for entry in entries:
        writer.writerow([
            entry.date.strftime('%Y-%m-%d'),
            entry.amount,
            entry.description or '',
            entry.notes or ''
        ])
    
    output = csvfile.getvalue()
    csvfile.close()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'cashflow_export_{timestamp}.csv'
    
    from flask import Response
    return Response(
        output,
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )


if __name__ == '__main__':
    print("\n" + "="*60)
    print("\033[1;33m🚀 MONEYPAL STARTING...\033[0m")
    print("\033[1;32m📱 OPEN http://127.0.0.1:5000/ IN YOUR BROWSER!\033[0m")
    print("\033[1;34m✔️ Server running — ready for requests.\033[0m")
    print("="*60 + "\n")
    app.run(debug=True)