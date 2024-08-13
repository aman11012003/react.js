#pip install sqlite3
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Commit changes
conn.commit()

# Function to create a new user (CREATE)
def create_user(name, age, email):
    cursor.execute('''
    INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    ''', (name, age, email))
    conn.commit()
    print("User created successfully.")

# Function to read users (READ)
def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Function to update a user's information (UPDATE)
def update_user(user_id, name=None, age=None, email=None):
    if name:
        cursor.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
    if age:
        cursor.execute('UPDATE users SET age = ? WHERE id = ?', (age, user_id))
    if email:
        cursor.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
    conn.commit()
    print("User updated successfully.")

# Function to delete a user (DELETE)
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print("User deleted successfully.")

# Example usage
if __name__ == "__main__":
    # Create users
    create_user('John Doe', 30, 'john@example.com')
    create_user('Jane Doe', 25, 'jane@example.com')

    # Read users
    print("Users:")
    read_users()

    # Update user
    update_user(1, age=31)

    # Read users after update
    print("Users after update:")
    read_users()

    # Delete user
    delete_user(2)

    # Read users after deletion
    print("Users after deletion:")
    read_users()

# Close the database connection when done
conn.close()
