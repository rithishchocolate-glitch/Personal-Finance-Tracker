import sqlite3

DB_FILENAME = "finance.db"

def generate_summary():
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()

    # Total income
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cur.fetchone()[0] or 0

    # Total expense
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = cur.fetchone()[0] or 0

    # Balance
    balance = total_income - total_expense

    print("=== Finance Summary ===")
    print(f"Total Income : {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance      : {balance}")

    # Optional: Summary by category
    print("\n=== Expense by Category ===")
    cur.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
    for row in cur.fetchall():
        print(f"{row[0]:<15} : {row[1]}")

    print("\n=== Income by Category ===")
    cur.execute("SELECT category, SUM(amount) FROM transactions WHERE type='income' GROUP BY category")
    for row in cur.fetchall():
        print(f"{row[0]:<15} : {row[1]}")

    conn.close()

if __name__ == "__main__":
    generate_summary()
