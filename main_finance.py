import sqlite3
from datetime import datetime, timedelta
import random

DB_FILENAME = "finance.db"

# --- Function to add a transaction ---
def add_transaction(date, t_type, category, amount):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (date, type, category, amount) VALUES (?, ?, ?, ?)",
        (date, t_type, category, amount)
    )
    conn.commit()
    print("Transaction added successfully with id:", cur.lastrowid)
    conn.close()

# --- Function to view all transactions ---
def view_transactions():
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions ORDER BY date")
    rows = cur.fetchall()
    print("ID | Date       | Type     | Category       | Amount")
    print("-"*50)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<8} | {row[3]:<13} | {row[4]}")
    conn.close()

# --- Function to generate summaries ---
def generate_summary():
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cur.fetchone()[0] or 0
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = cur.fetchone()[0] or 0
    balance = total_income - total_expense

    print("=== Finance Summary ===")
    print(f"Total Income : {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance      : {balance}")

    print("\n=== Expense by Category ===")
    cur.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
    for row in cur.fetchall():
        print(f"{row[0]:<15} : {row[1]}")

    print("\n=== Income by Category ===")
    cur.execute("SELECT category, SUM(amount) FROM transactions WHERE type='income' GROUP BY category")
    for row in cur.fetchall():
        print(f"{row[0]:<15} : {row[1]}")

    conn.close()

# --- Advanced Features ---
def filter_transactions_by_date(start_date, end_date):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM transactions WHERE date BETWEEN ? AND ? ORDER BY date",
        (start_date, end_date)
    )
    rows = cur.fetchall()
    print(f"Transactions from {start_date} to {end_date}:")
    print("ID | Date       | Type     | Category       | Amount")
    print("-"*50)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<8} | {row[3]:<13} | {row[4]}")
    conn.close()

def filter_transactions_by_category(category):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM transactions WHERE category=? ORDER BY date",
        (category,)
    )
    rows = cur.fetchall()
    print(f"Transactions in category '{category}':")
    print("ID | Date       | Type     | Category       | Amount")
    print("-"*50)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<8} | {row[3]:<13} | {row[4]}")
    conn.close()

def monthly_summary(month, year):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT type, SUM(amount) FROM transactions WHERE strftime('%Y', date)=? AND strftime('%m', date)=? GROUP BY type",
        (str(year), f"{month:02d}")
    )
    results = cur.fetchall()
    income = 0
    expense = 0
    for row in results:
        if row[0] == "income":
            income = row[1]
        else:
            expense = row[1]
    balance = (income or 0) - (expense or 0)
    print(f"Monthly Summary for {year}-{month:02d}")
    print(f"Total Income : {income or 0}")
    print(f"Total Expense: {expense or 0}")
    print(f"Balance      : {balance}")
    conn.close()

# --- Main Menu ---
def main_menu():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add a Transaction")
        print("2. View All Transactions")
        print("3. Generate Summary")
        print("4. Advanced Features (Filter / Monthly)")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            t_type = input("Enter type (income/expense): ").lower()
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_transaction(date, t_type, category, amount)
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            generate_summary()
        elif choice == "4":
            print("\n--- Advanced Features ---")
            print("1. Filter by Date")
            print("2. Filter by Category")
            print("3. Monthly Summary")
            adv_choice = input("Choose an option (1/2/3): ")
            if adv_choice == "1":
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                filter_transactions_by_date(start_date, end_date)
            elif adv_choice == "2":
                category = input("Category: ")
                filter_transactions_by_category(category)
            elif adv_choice == "3":
                month = int(input("Month (1-12): "))
                year = int(input("Year (YYYY): "))
                monthly_summary(month, year)
            else:
                print("Invalid choice!")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main_menu()
