import sqlite3
import os

# Add account_type column to existing database
db_path = os.path.join(os.path.dirname(__file__), 'cashflow.db')

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if column already exists
    cursor.execute("PRAGMA table_info(cashflow)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'account_type' not in columns:
        # Add the column with default value 'bank'
        cursor.execute("ALTER TABLE cashflow ADD COLUMN account_type TEXT DEFAULT 'bank'")
        # Update all existing records to 'bank'
        cursor.execute("UPDATE cashflow SET account_type = 'bank' WHERE account_type IS NULL")
        conn.commit()
        print("Added account_type column to existing database")
    else:
        print("account_type column already exists")
    
    conn.close()
else:
    print("Database does not exist yet")