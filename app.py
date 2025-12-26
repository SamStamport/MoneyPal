from flask import Flask, render_template, request, jsonify, Response
from datetime import datetime, date, timedelta
from models import db, CashFlow, ACCOUNT_TYPE_BANK, ACCOUNT_TYPE_SECURED_VISA
from sqlalchemy import func
from io import StringIO
import csv
import os
import json

try:
    import pandas as pd
except ImportError:
    pd = None

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
    print("Database initialized - loading complete.")


@app.route('/', methods=['GET'])
def index():
    from flask import redirect, url_for
    return redirect(url_for('list_entries'))


@app.route('/cashflow', methods=['GET'])
def list_entries():
    entries = CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_BANK).order_by(CashFlow.date.desc()).all()
    
    # Calculate running balance
    running_balance = 0
    entries_with_balance = []
    for entry in reversed(entries):  # Start from oldest
        running_balance += entry.amount
        entries_with_balance.append({
            'entry': entry,
            'balance': running_balance
        })
    
    entries_with_balance.reverse()  # Back to newest first
    return render_template('cashflow.html', entries_with_balance=entries_with_balance)


@app.route('/secured-visa', methods=['GET'])
def secured_visa():
    entries = CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_SECURED_VISA).order_by(CashFlow.date.desc()).all()
    
    # Calculate running balance
    running_balance = 0
    entries_with_balance = []
    for entry in reversed(entries):  # Start from oldest
        running_balance += entry.amount
        entries_with_balance.append({
            'entry': entry,
            'balance': running_balance
        })
    
    entries_with_balance.reverse()  # Back to newest first
    return render_template('secured_visa.html', entries_with_balance=entries_with_balance)


@app.route('/charts', methods=['GET'])
def charts():
    """Display interactive charts for cash flow analysis and projections"""
    
    # Get all entries for both accounts, sorted by date
    bank_entries = CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_BANK).order_by(CashFlow.date).all()
    visa_entries = CashFlow.query.filter_by(account_type=ACCOUNT_TYPE_SECURED_VISA).order_by(CashFlow.date).all()
    
    # Calculate running balances for bank account
    bank_data = []
    running_balance = 0
    for entry in bank_entries:
        running_balance += entry.amount
        bank_data.append({
            'date': entry.date.strftime('%Y-%m-%d'),
            'balance': round(running_balance, 2)
        })
    
    # Calculate running balances for secured visa
    visa_data = []
    running_balance = 0
    for entry in visa_entries:
        running_balance += entry.amount
        visa_data.append({
            'date': entry.date.strftime('%Y-%m-%d'),
            'balance': round(running_balance, 2)
        })
    
    # Calculate projections (30 days into future)
    bank_projection, bank_accuracy = calculate_projection_prophet(bank_entries, ACCOUNT_TYPE_BANK, days=30)
    visa_projection, visa_accuracy = calculate_projection_prophet(visa_entries, ACCOUNT_TYPE_SECURED_VISA, days=30)
    
    return render_template('charts.html', 
                         bank_data=json.dumps(bank_data),
                         visa_data=json.dumps(visa_data),
                         bank_projection=json.dumps(bank_projection),
                         visa_projection=json.dumps(visa_projection),
                         bank_accuracy=bank_accuracy,
                         visa_accuracy=visa_accuracy)


def calculate_projection_prophet(entries, account_type, days=30):
    """Calculate future balance projection using Prophet for time series forecasting"""
    
    # Need at least 10 data points for Prophet
    if len(entries) < 10 or pd is None:
        return calculate_projection_simple(entries, account_type, days)
    
    try:
        from prophet import Prophet
        
        # Prepare data for Prophet (needs 'ds' for date and 'y' for value)
        data = []
        running_balance = 0
        for entry in entries:
            running_balance += entry.amount
            data.append({
                'ds': entry.date,
                'y': running_balance
            })
        
        df = pd.DataFrame(data)
        
        # Initialize and fit Prophet model
        # Disable yearly seasonality (not enough data), enable weekly and daily
        model = Prophet(
            daily_seasonality=False,
            weekly_seasonality=True,
            yearly_seasonality=False,
            changepoint_prior_scale=0.05  # Lower = less flexible, more stable predictions
        )
        
        # Suppress Prophet's verbose output
        import logging
        logging.getLogger('prophet').setLevel(logging.WARNING)
        
        model.fit(df)
        
        # Create future dataframe
        future = model.make_future_dataframe(periods=days)
        forecast = model.predict(future)
        
        # Extract only future predictions (after last historical date)
        last_date = df['ds'].max()
        future_forecast = forecast[forecast['ds'] > last_date]
        
        # Calculate accuracy based on uncertainty intervals
        # Prophet provides yhat_lower and yhat_upper (80% confidence interval)
        avg_uncertainty = (future_forecast['yhat_upper'] - future_forecast['yhat_lower']).mean()
        avg_prediction = future_forecast['yhat'].mean()
        
        # Convert uncertainty to accuracy percentage
        # Lower uncertainty relative to prediction = higher accuracy
        if avg_prediction != 0:
            uncertainty_ratio = (avg_uncertainty / abs(avg_prediction)) * 100
            accuracy = max(0, min(100, 100 - uncertainty_ratio))
        else:
            accuracy = 50  # Default if prediction is near zero
        
        # Format projection data
        projection = []
        for _, row in future_forecast.iterrows():
            projection.append({
                'date': row['ds'].strftime('%Y-%m-%d'),
                'balance': round(row['yhat'], 2),
                'lower': round(row['yhat_lower'], 2),
                'upper': round(row['yhat_upper'], 2)
            })
        
        return projection, round(accuracy, 1)
        
    except ImportError:
        # Prophet not installed, fall back to simple method
        print("⚠️  Prophet not installed. Using simple projection method.")
        print("   Install with: pip install prophet")
        return calculate_projection_simple(entries, account_type, days)
    except Exception as e:
        # Any other error, fall back to simple method
        print(f"⚠️  Prophet error: {e}. Using simple projection method.")
        return calculate_projection_simple(entries, account_type, days)


def calculate_projection_simple(entries, account_type, days=30):
    """Fallback: Simple projection based on recent average (original method)"""
    if len(entries) < 2:
        return [], 0
    
    # Use last 30 days of data to calculate average daily change
    recent_date = datetime.now().date() - timedelta(days=30)
    recent_entries = [e for e in entries if e.date >= recent_date]
    
    if len(recent_entries) < 2:
        recent_entries = entries[-10:] if len(entries) >= 10 else entries
    
    # Calculate average daily change
    if len(recent_entries) > 0:
        total_change = sum(e.amount for e in recent_entries)
        days_span = (recent_entries[-1].date - recent_entries[0].date).days or 1
        avg_daily_change = total_change / days_span
    else:
        avg_daily_change = 0
    
    # Get current balance
    current_balance = sum(e.amount for e in entries)
    last_date = entries[-1].date if entries else datetime.now().date()
    
    # Generate projection
    projection = []
    for i in range(1, days + 1):
        proj_date = last_date + timedelta(days=i)
        proj_balance = current_balance + (avg_daily_change * i)
        projection.append({
            'date': proj_date.strftime('%Y-%m-%d'),
            'balance': round(proj_balance, 2)
        })
    
    # Simple method has lower accuracy (estimate 60-70%)
    accuracy = 65.0
    
    return projection, accuracy


@app.route('/add-ajax', methods=['POST'])
def add_entry_ajax():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('date') or not data.get('amount'):
            return jsonify({'error': 'Date and amount are required'}), 400
        
        # Validate and parse date
        try:
            date_obj = datetime.strptime(data['date'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), 400
        
        # Validate and parse amount
        try:
            amount = float(data['amount'])
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid amount'}), 400
        
        description = data.get('description', '')
        notes = data.get('notes', '')
        account_type = data.get('account_type', ACCOUNT_TYPE_BANK)
        
        # Validate account type
        if account_type not in [ACCOUNT_TYPE_BANK, ACCOUNT_TYPE_SECURED_VISA]:
            return jsonify({'error': 'Invalid account type'}), 400

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
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/update/<int:entry_id>', methods=['POST'])
def update_entry(entry_id):
    try:
        data = request.get_json()
        entry = CashFlow.query.get_or_404(entry_id)

        if 'date' in data:
            try:
                entry.date = datetime.strptime(data['date'], "%Y-%m-%d").date()
            except ValueError:
                return jsonify({'error': 'Invalid date format'}), 400
                
        if 'amount' in data:
            try:
                entry.amount = float(data['amount'])
            except (ValueError, TypeError):
                return jsonify({'error': 'Invalid amount'}), 400
                
        if 'description' in data:
            entry.description = data['description']
            
        if 'notes' in data:
            entry.notes = data['notes']

        db.session.commit()
        return jsonify({'success': True}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/delete/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    try:
        entry = CashFlow.query.get_or_404(entry_id)
        db.session.delete(entry)
        db.session.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/export-csv', methods=['GET'])
def export_cashflow_csv():
    account_type = request.args.get('account_type', ACCOUNT_TYPE_BANK)
    
    entries = CashFlow.query.filter_by(account_type=account_type).order_by(CashFlow.date).all()
    
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
    account_name = 'bank' if account_type == ACCOUNT_TYPE_BANK else 'secured_visa'
    filename = f'cashflow_export_{account_name}_{timestamp}.csv'
    
    return Response(
        output,
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )


if __name__ == '__main__':
    print("\n" + "="*60)
    print("MONEYPAL STARTING...")
    print("OPEN http://127.0.0.1:5000/ IN YOUR BROWSER!")
    print("Server running - ready for requests.")
    print("="*60 + "\n")
    app.run(debug=True)