import sqlite3
import random
from datetime import datetime, timedelta

DB_FILENAME = "finance.db"

income_categories = ["salary", "freelancing", "bonus"]
expense_categories = ["food", "rent", "entertainment", "shopping", "transport"]

def add_transaction(date, t_type, category, amount):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (date, type, category, amount) VALUES (?, ?, ?, ?)",
        (date, t_type, category, amount)
    )
    conn.commit()
    conn.close()

def generate_sample_transactions(n=100):
    start_date = datetime(2025, 1, 1)
    for _ in range(n):
        delta_days = random.randint(0, 364)
        date = (start_date + timedelta(days=delta_days)).strftime("%Y-%m-%d")
        t_type = random.choice(["income", "expense"])
        if t_type == "income":
            category = random.choice(income_categories)
            amount = random.randint(500, 5000)
        else:
            category = random.choice(expense_categories)
            amount = random.randint(50, 1000)
        add_transaction(date, t_type, category, amount)
    print(f"{n} sample transactions inserted successfully.")

if __name__ == "__main__":
    generate_sample_transactions(100)
