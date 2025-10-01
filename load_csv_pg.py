import psycopg2
import csv
from datetime import datetime
import logging

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 replace with your password
DB_HOST = "localhost"
DB_PORT = "5432"

# Setup logging (writes messages into a file: errors.log)
logging.basicConfig(
    filename="errors.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_transaction(date, t_type, category, amount):
    """Validate a transaction row before inserting"""

    # 1. Validate date
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        msg = f"Invalid date: {date}"
        print(f"❌ Skipping row: {msg}")
        logging.warning(msg)
        return False

    # 2. Validate type
    if t_type not in ["income", "expense"]:
        msg = f"Invalid type: {t_type}"
        print(f"❌ Skipping row: {msg}")
        logging.warning(msg)
        return False

    # 3. Validate amount
    try:
        amount = float(amount)
        if amount <= 0:
            msg = f"Non-positive amount: {amount}"
            print(f"❌ Skipping row: {msg}")
            logging.warning(msg)
            return False
    except ValueError:
        msg = f"Invalid amount: {amount}"
        print(f"❌ Skipping row: {msg}")
        logging.warning(msg)
        return False

    # 4. Validate category
    if not category.strip():
        msg = "Empty category"
        print(f"❌ Skipping row: {msg}")
        logging.warning(msg)
        return False

    return True

def load_csv(filename):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if validate_transaction(row["date"], row["type"], row["category"], row["amount"]):
                cur.execute(
                    "INSERT INTO transactions (date, type, category, amount) VALUES (%s, %s, %s, %s)",
                    (row["date"], row["type"], row["category"], float(row["amount"]))
                )

    conn.commit()
    print("✅ CSV data loaded successfully (invalid rows skipped).")
    cur.close()
    conn.close()

if __name__ == "__main__":
    load_csv("transactions.csv")
