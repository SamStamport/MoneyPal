# app.py
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from models import db, CashFlow
from ideas_capture import add_idea_route

app = Flask(__name__)

# Configure database URI and disable track modifications for performance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cashflow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB tables if they don't exist yet
with app.app_context():
    db.create_all()

# Add idea capture routes
add_idea_route(app)


@app.route('/', methods=['GET'])
def list_entries():
    # Fetch all entries ordered by date ascending
    entries = CashFlow.query.order_by(CashFlow.date).all()
    return render_template('cashflow.html', entries=entries)

@app.route('/add-ajax', methods=['POST'])
def add_entry_ajax():
    try:
        data = request.get_json()
        date_obj = datetime.strptime(data['date'], "%Y-%m-%d").date()
        amount = float(data['amount'])
        description = data.get('description', '')
        category = data.get('category', '')
        notes = data.get('notes', '')

        new_entry = CashFlow(
            date=date_obj,
            amount=amount,
            description=description,
            category=category,
            notes=notes
        )
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({
            'id': new_entry.id,
            'date': new_entry.date.strftime("%Y-%m-%d"),
            'amount': new_entry.amount,
            'description': new_entry.description,
            'category': new_entry.category,
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
        if 'category' in data:
            entry.category = data['category']
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


if __name__ == '__main__':
    app.run(debug=True)
