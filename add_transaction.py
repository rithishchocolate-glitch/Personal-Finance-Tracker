import psycopg2
from datetime import datetime

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

def validate_transaction(date, t_type, category, amount):
    """Validate transaction before inserting into DB"""

    # 1. Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return False

    # 2. Validate type
    if t_type not in ["income", "expense"]:
        print("❌ Type must be 'income' or 'expense'.")
        return False

    # 3. Validate amount
    try:
        amount = float(amount)
        if amount <= 0:
            print("❌ Amount must be positive.")
            return False
    except ValueError:
        print("❌ Amount must be a number.")
        return False

    # 4. Validate category
    if not category.strip():
        print("❌ Category cannot be empty.")
        return False

    return True

def add_transaction(date, t_type, category, amount):
    """Insert transaction if valid"""
    if not validate_transaction(date, t_type, category, amount):
        return

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (date, type, category, amount) VALUES (%s, %s, %s, %s)",
        (date, t_type, category, float(amount))
    )
    conn.commit()
    print("✅ Transaction added successfully.")
    cur.close()
    conn.close()

def main():
    print("=== Add a New Transaction ===")
    date = input("Enter date (YYYY-MM-DD): ")
    t_type = input("Enter type (income/expense): ").lower()
    category = input("Enter category (e.g., food, rent, salary): ")
    amount = input("Enter amount: ")

    add_transaction(date, t_type, category, amount)

if __name__ == "__main__":
    main()
