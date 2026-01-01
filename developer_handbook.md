# Developer Handbook

## Overview
A comprehensive guide for development practices, tools, and workflows.    

Here’s a **tight, documentation-ready summary** you can drop straight into your app docs. I’ve kept it procedural, neutral in tone, and assumption-free.

---

## Importing a One-Time CSV Batch into SQLite

When a CSV file does not contain all columns required by the destination table, use a temporary import table and populate missing fields during insertion.

### 1. Create a temporary import table matching the CSV

The temporary table must match the CSV column names and order exactly.

```sql
CREATE TABLE import_txn (
    date TEXT,
    description TEXT,
    amount REAL
);
```

### 2. Import the CSV into the temporary table

* Use **File → Import → Table from CSV file…**
* Select `import_txn`
* Enable **Column names in first line**
* Save changes

### 3. Insert into the destination table

Insert only the columns present in the CSV. Missing columns are automatically set to `NULL`, and the primary key is auto-generated.

```sql
INSERT INTO transactions (date, amount, description)
SELECT date, amount, description
FROM import_txn;
```

### 4. Set a default value for this batch

Assign a fixed value to missing columns for this import batch only.

```sql
UPDATE transactions
SET account_type = 'bank'
WHERE account_type IS NULL;
```

### 5. (Optional) Clean up

Remove the temporary table after verification.

```sql
DROP TABLE import_txn;
```

---

### Notes

* Do not modify the CSV to add dummy columns.
* Do not rely on column position in the destination table.
* This approach avoids schema changes and keeps one-time imports isolated and repeatable.

---



## Quick Commands

### Backup
- **PowerShell**: `.\backup`
- **Command Prompt**: `backup`

## Development Workflow

### Git Commands
```bash
git add .
git commit -m "message"
git push origin master
```

### Project Structure
- Keep backup scripts in all project directories
- Use consistent naming conventions
- Document all major changes

## Tools & Scripts

### Backup Script
- Automatically stages, commits, and pushes changes
- Handles clean working tree scenarios
- Works across all project directories

## Best Practices
- Always test scripts before deployment
- Keep documentation updated
- Use meaningful commit messages