# wex-2025
Work Experience 2025 - Subscription Manager

# Python Virtual Environment Setup

To create and activate a virtual environment in Python, follow these steps:

1. Create a virtual environment:
Run this command in your project directory:
    python -m venv venv

2. Activate the virtual environment:
Windows command prompt:
    venv\Scripts\activate

MacOS and Linux:
    source venv/bin/activate

3. Installing Dependancies
If you have a requirements.txt, install the dependancies with
    pip install -r requirements.txt

4. Deactivate the Virtual Environment
To exit the virtual environment:
    deactivate

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
