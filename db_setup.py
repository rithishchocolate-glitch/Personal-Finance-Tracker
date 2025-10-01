# db_setup.py
# Step 1: create a SQLite database file and a 'transactions' table

import sqlite3
import os

DB_FILENAME = "finance.db"

def create_connection(db_file=DB_FILENAME):
    """
    Connect to (or create) the SQLite database file and return the connection.
    The file will be created in the same folder as this script.
    """
    conn = sqlite3.connect(db_file)
    return conn

def create_transactions_table(conn):
    """
    Create the transactions table if it doesn't already exist.
    Columns:
      - id: integer primary key, auto increment
      - date: text (store as YYYY-MM-DD)
      - type: 'income' or 'expense' (stored as text)
      - category: text (e.g., food, rent, salary)
      - amount: real number (e.g., 500.0)
    """
    sql = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL
    );
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def show_tables(conn):
    """Print tables currently in the database (simple check)."""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()
    print("Tables in database:", rows)

def main():
    print("This script will create (or open) the database file:", os.path.abspath(DB_FILENAME))
    conn = create_connection()
    create_transactions_table(conn)
    show_tables(conn)
    conn.close()
    print("Done. 'transactions' table is ready in", DB_FILENAME)

if __name__ == "__main__":
    main()
