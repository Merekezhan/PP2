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



# Procedure to delete data by username or phone
def delete_from_phonebook(username=None, phone=None):
    conn = connect_to_database()
    cur = conn.cursor()
    if username:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (username,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        raise ValueError("Both username and phone cannot be None.")
    conn.commit()
    cur.close()
    conn.close()


# Delete data by username or phone
delete_from_phonebook(username='John')
delete_from_phonebook(phone='9876543210')
