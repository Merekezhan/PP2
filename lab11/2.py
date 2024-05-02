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



# Procedure to insert new user or update if exists
def insert_or_update_user(first_name, last_name, phone):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM phonebook WHERE first_name = %s)", (first_name,))
    exists = cur.fetchone()[0]
    if exists:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (phone, first_name))
    else:
        cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()



# Insert or update a user
insert_or_update_user('John', 'Doe', '1234567890')

