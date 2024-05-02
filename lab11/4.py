import psycopg2

# Function to connect to the database
def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="Merekezhan06@"
    )
    return conn


# Function for pagination
def get_phonebook_with_pagination(limit, offset):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY first_name LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows



# Query data with pagination
pagination_results = get_phonebook_with_pagination(limit=5, offset=0)
print(pagination_results)

