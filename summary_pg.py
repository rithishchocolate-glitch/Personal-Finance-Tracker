import psycopg2

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

def show_summary():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    # Total income
    cur.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'income';")
    total_income = cur.fetchone()[0]

    # Total expense
    cur.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'expense';")
    total_expense = cur.fetchone()[0]

    # Balance
    balance = total_income - total_expense

    # Category-wise totals
    cur.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        GROUP BY category
        ORDER BY SUM(amount) DESC;
    """)
    category_totals = cur.fetchall()

    # Print results
    print("=== Finance Summary ===")
    print(f"Total Income : {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance      : {balance}")
    print("\n--- Category Totals ---")
    for category, total in category_totals:
        print(f"{category}: {total}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    show_summary()
