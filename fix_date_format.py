#!/usr/bin/env python3
"""
Fix corrupted date formats in the database.
This script will find and fix any dates that are not in ISO format.
"""

import sqlite3
import os
from datetime import datetime
import html

def fix_database_dates(db_path):
    """Fix corrupted date formats in the database"""
    if not os.path.exists(db_path):
        print(f"Database not found: {db_path}")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Get all records with their current dates
        cursor.execute("SELECT id, date FROM cashflow")
        records = cursor.fetchall()
        
        fixed_count = 0
        
        for record_id, date_str in records:
            try:
                # Try to parse as ISO date first
                datetime.strptime(date_str, '%Y-%m-%d')
                # If successful, date is already in correct format
                continue
            except ValueError:
                # Date needs fixing
                try:
                    # Decode HTML entities first
                    clean_date = html.unescape(date_str)
                    
                    # Try common date formats
                    date_obj = None
                    for fmt in ['%m/%d/%Y', '%m/%d/%y', '%d/%m/%Y', '%d/%m/%y']:
                        try:
                            date_obj = datetime.strptime(clean_date, fmt)
                            break
                        except ValueError:
                            continue
                    
                    if date_obj:
                        # Convert to ISO format
                        iso_date = date_obj.strftime('%Y-%m-%d')
                        cursor.execute("UPDATE cashflow SET date = ? WHERE id = ?", (iso_date, record_id))
                        print(f"Fixed record {record_id}: '{date_str}' -> '{iso_date}'")
                        fixed_count += 1
                    else:
                        print(f"Could not parse date for record {record_id}: '{date_str}'")
                        
                except Exception as e:
                    print(f"Error processing record {record_id}: {e}")
        
        conn.commit()
        print(f"\nFixed {fixed_count} date records in {db_path}")
        
    except Exception as e:
        print(f"Error accessing database: {e}")
        conn.rollback()
    finally:
        conn.close()

def main():
    # Fix both databases
    script_dir = os.path.dirname(__file__)
    
    databases = [
        os.path.join(script_dir, 'cashflowlive.db'),
        os.path.join(script_dir, 'cashflowtest.db')
    ]
    
    for db_path in databases:
        if os.path.exists(db_path):
            print(f"\nFixing dates in: {db_path}")
            fix_database_dates(db_path)
        else:
            print(f"Database not found: {db_path}")

if __name__ == '__main__':
    main()