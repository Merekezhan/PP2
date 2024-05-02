import psycopg2
import csv

# Function to insert data from CSV file
def insert_from_csv(filename, cursor, conn):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)  # Skip header row
            if header is None:
                print("CSV file is empty.")
                return
            for row in csv_reader:
                cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", row)
        conn.commit()
        print("Data inserted from CSV file successfully.")
    except IOError as e:
        print(f"Error reading CSV file: {e}")

# Function to insert data from console
def insert_from_console(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    print("Data inserted from console successfully.")

# Function to update data in the table
def update_data(username, new_phone, cursor, conn):
    cursor.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s OR last_name = %s", (new_phone, username, username))
    conn.commit()
    print("Data updated successfully.")

# Function to query data from the table
def query_data(filter_type, filter_value, cursor):
    if filter_type == 'first_name':
        cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == 'last_name':
        cursor.execute("SELECT * FROM phonebook WHERE last_name = %s", (filter_value,))
    elif filter_type == 'phone':
        cursor.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("Invalid filter type.")
        return

    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("No matching records found.")

# Function to delete data from the table
def delete_data(filter_type, filter_value, cursor, conn):
    if filter_type == 'first_name':
        cursor.execute("DELETE FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == 'last_name':
        cursor.execute("DELETE FROM phonebook WHERE last_name = %s", (filter_value,))
    elif filter_type == 'phone':
        cursor.execute("DELETE FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("Invalid filter type.")
        return

    conn.commit()
    print("Data deleted successfully.")

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="Merekezhan06@"
    )
    cursor = conn.cursor()

    # Create PhoneBook table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                        id SERIAL PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        phone TEXT UNIQUE
                    )''')

    # Sample usage of your functions
    insert_from_csv('phone_book.csv', cursor, conn)
    insert_from_console(cursor, conn)
    update_data('John', '1234567890', cursor, conn)
    query_data('first_name', 'John', cursor)
    delete_data('phone', '1234567890', cursor, conn)

    # Close database connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)