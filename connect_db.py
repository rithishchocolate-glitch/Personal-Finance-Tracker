import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    database="finance_db",  # your database name
    user="postgres",        # default username
    password="bunny",# your PostgreSQL password
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT version();")
db_version = cur.fetchone()
print("Connected to PostgreSQL, version:", db_version)

conn.close()
