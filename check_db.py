import sqlite3

# Check what's in the database
conn = sqlite3.connect('cashflow.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:", [t[0] for t in tables])

# Check cash_flow table (with underscore)
if ('cash_flow',) in tables:
    cursor.execute("SELECT COUNT(*) FROM cash_flow")
    count = cursor.fetchone()[0]
    print(f"Total rows in cash_flow: {count}")
    
    if count > 0:
        cursor.execute("SELECT date, amount, description, category FROM cash_flow ORDER BY date LIMIT 5")
        rows = cursor.fetchall()
        print("First 5 rows:")
        for row in rows:
            print(f"  {row[0]}: {row[1]:.2f} - {row[2]} ({row[3]})")
else:
    print("cash_flow table does not exist")

conn.close()
