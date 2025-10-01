user="postgres",
password="bunny",
import psycopg2

def create_table():
    conn = psycopg2.connect(
        database="finance_db",   # must match the db you created in pgAdmin
        user="postgres",         # default user
        password="bunny", # replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            type VARCHAR(10) NOT NULL,
            category VARCHAR(50),
            amount NUMERIC(10,2) NOT NULL
        );
    """)

    conn.commit()
    print("Table created successfully.")
    conn.close()

if __name__ == "__main__":
    create_table()
