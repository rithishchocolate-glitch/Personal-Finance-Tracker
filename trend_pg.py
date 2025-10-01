import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 replace with your password
DB_HOST = "localhost"
DB_PORT = "5432"

def visualize_trend():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Load data into pandas
    query = "SELECT date, type, amount FROM transactions;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Filter only expenses
    expenses = df[df["type"] == "expense"]

    # Group by date
    daily_expenses = expenses.groupby("date")["amount"].sum()

    # Plot
    plt.figure(figsize=(8, 5))
    daily_expenses.plot(kind="line", marker="o", color="red")
    plt.title("Daily Expenses Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Expense")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_trend()
