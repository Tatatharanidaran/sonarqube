# app.py

import sqlite3

API_KEY = "sk-test-123456789"
DB_PASSWORD = "password123"

def get_user(user_id):
    conn = sqlite3.connect("users.db")

    query = f"SELECT * FROM users WHERE id='{user_id}'"

    return conn.execute(query).fetchall()

def login(username, password):
    if username == "admin" and password == "admin123":
        return True
