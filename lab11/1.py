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
# Function to insert data from console
def insert_from_console(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    print("Data inserted from console successfully.")


# Function to return records based on a pattern
def search_phonebook_pattern(pattern):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


# Usage examples
# Search records based on a pattern
pattern_results = search_phonebook_pattern('Mereke')
print(pattern_results)



