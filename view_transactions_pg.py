import psycopg2

DB_NAME = "finance_db"
DB_USER = "postgres"
DB_PASSWORD = "bunny"   # 🔹 Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

def view_transactions():
    """Fetch and display all transactions"""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    view_transactions()
