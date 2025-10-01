import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 replace with your password
DB_HOST = "localhost"
DB_PORT = "5432"

def visualize_expenses():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Read transactions into a pandas DataFrame
    query = "SELECT * FROM transactions;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Filter only expenses
    expenses = df[df["type"] == "expense"]

    # Group by category
    category_totals = expenses.groupby("category")["amount"].sum().sort_values(ascending=False)

    # Plot
    plt.figure(figsize=(8, 5))
    category_totals.plot(kind="bar", color="skyblue")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_expenses()
