import sqlite3

DB_FILENAME = "finance.db"

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

if __name__ == "__main__":
    print("=== Advanced Features ===")
    print("1. Filter by Date")
    print("2. Filter by Category")
    print("3. Monthly Summary")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        start_date = input("Start Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        filter_transactions_by_date(start_date, end_date)
    elif choice == "2":
        category = input("Category: ")
        filter_transactions_by_category(category)
    elif choice == "3":
        month = int(input("Month (1-12): "))
        year = int(input("Year (YYYY): "))
        monthly_summary(month, year)
    else:
        print("Invalid choice!")
