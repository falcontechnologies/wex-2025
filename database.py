# This program creates a SQLite database to manage:
# - Users
# - Subscriptions
# - Payment Methods
# - Transcation History

# Author: aaronqwang
# Date: March 4th, 2025


# Connect to the database
import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()


# Create user table
c.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    )
""")


# Create subscription table
# 0: False
# 1: True
c.execute("""
    CREATE TABLE IF NOT EXISTS subscription (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        service_provider TEXT,
        start_date TIMESTAMP NOT NULL,
        expiry_date TIMESTAMP,
        is_trial INTEGER NOT NULL CHECK (is_trial IN (0,1)),  
        is_recurring INTEGER NOT NULL CHECK (is_recurring IN (0,1)), 
        payment_frequency TEXT NOT NULL,
        cost REAL,
        status TEXT NOT NULL,
        subscription_type TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    )
""")


# Create payment_method table
c.execute("""
    CREATE TABLE IF NOT EXISTS payment_method (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    )
""")

# Create transcation_history table
c.execute("""
    CREATE TABLE IF NOT EXISTS transaction_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subscription_id INTEGER,
        payment_id INTEGER,
        amount_paid REAL NOT NULL,
        date_paid TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (subscription_id) REFERENCES subscription(id) ON DELETE CASCADE,
        FOREIGN KEY (payment_id) REFERENCES payment_method(id) ON DELETE CASCADE
    )
""")


conn.commit()
conn.close()