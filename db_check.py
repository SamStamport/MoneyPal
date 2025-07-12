import sqlite3
import os

print("\n=== Database Check Script ===")

# Get the database path
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'moneypal.db')
print(f"Database path: {DB_PATH}")

# Check if database file exists
if not os.path.exists(DB_PATH):
    print("Database file not found!")
else:
    print("Database file found!")
    
    # Connect to the database
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        print("\nChecking database tables:")
        # Get table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if tables:
            print("\nTables in database:")
            for table in tables:
                print(f"- {table[0]}")
                
                # Get table column names
                cursor.execute(f"PRAGMA table_info({table[0]})")
                columns = cursor.fetchall()
                print("  Columns:")
                for column in columns:
                    print(f"  - {column[1]} ({column[2]})")
        else:
            print("No tables found in database")
            
        conn.close()
        print("\nDatabase check completed successfully!")
        
    except Exception as e:
        print(f"Error accessing database: {str(e)}")
