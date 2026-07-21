import psycopg
print(psycopg.__version__)
conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="mtg_collection",
    user="postgres",
    password="DAJ2fredrick!"
)

with conn.cursor() as cur:
    cur.execute("SELECT version();")
    print(cur.fetchone())

conn.close()