# wex-2025
Work Experience 2025 - Subscription Manager

# Python Database Connection Set Up

To set up a Python database connection, follow these steps

pip install sqlite3 #SQLite(comes with Python)

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('customer.db')

# Create a cursor for SQL commands
c = conn.cursor()

# Create a table if it doesn't already exist
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number TEXT
)
""")

# Inserting data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Retrieving data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Closing connection
c.close()
conn.close()
