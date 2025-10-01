import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 replace with your PostgreSQL password
DB_HOST = "localhost"
DB_PORT = "5432"

# ==============================
# Database Helper
# ==============================
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# ==============================
# Add Transaction
# ==============================
def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    t_type = input("Enter type (income/expense): ").lower()
    category = input("Enter category (e.g., food, rent, salary): ")
    amount = float(input("Enter amount: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (date, type, category, amount) VALUES (%s, %s, %s, %s)",
        (date, t_type, category, amount)
    )
    conn.commit()
    print("✅ Transaction added successfully.")
    cur.close()
    conn.close()

# ==============================
# View Transactions
# ==============================
def view_transactions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions ORDER BY date;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# ==============================
# Summary
# ==============================
def show_summary():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COALESCE(SUM(amount),0) FROM transactions WHERE type='income';")
    total_income = cur.fetchone()[0]

    cur.execute("SELECT COALESCE(SUM(amount),0) FROM transactions WHERE type='expense';")
    total_expense = cur.fetchone()[0]

    balance = total_income - total_expense

    cur.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        GROUP BY category
        ORDER BY SUM(amount) DESC;
    """)
    category_totals = cur.fetchall()

    print("\n=== Finance Summary ===")
    print(f"Total Income : {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance      : {balance}")
    print("\n--- Category Totals ---")
    for category, total in category_totals:
        print(f"{category}: {total}")

    cur.close()
    conn.close()

# ==============================
# Visualization
# ==============================
def visualize_expenses():
    conn = get_connection()
    query = "SELECT * FROM transactions;"
    df = pd.read_sql(query, conn)
    conn.close()

    expenses = df[df["type"] == "expense"]
    category_totals = expenses.groupby("category")["amount"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))
    category_totals.plot(kind="bar", color="skyblue")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_trend():
    conn = get_connection()
    query = "SELECT date, type, amount FROM transactions;"
    df = pd.read_sql(query, conn)
    conn.close()

    expenses = df[df["type"] == "expense"]
    daily_expenses = expenses.groupby("date")["amount"].sum()

    plt.figure(figsize=(8,5))
    daily_expenses.plot(kind="line", marker="o", color="red")
    plt.title("Daily Expenses Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Expense")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ==============================
# Main Menu
# ==============================
def main():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Visualize Expenses by Category")
        print("5. Visualize Daily Expense Trend")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            visualize_expenses()
        elif choice == "5":
            visualize_trend()
        elif choice == "6":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
