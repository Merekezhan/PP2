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


# Procedure to insert many new users and check correctness of phones
def insert_many_users(users_list):
    conn = connect_to_database()
    cur = conn.cursor()
    incorrect_data = []
    for user in users_list:
        first_name, last_name, phone = user.split(',')
        if len(phone.strip()) != 10:  # Assuming phone number length is 10 digits
            incorrect_data.append((first_name, last_name, phone))
        else:
            cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name.strip(), last_name.strip(), phone.strip()))
    conn.commit()
    cur.close()
    conn.close()
    return incorrect_data



# Insert many new users
incorrect_data = insert_many_users(['Jane,Doe,123456789', 'Bob,Smith,9876543210'])

