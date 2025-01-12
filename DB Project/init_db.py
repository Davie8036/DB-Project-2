# filepath: /c:/Users/Home/Desktop/DB Project/init_db.py
import os
import sqlite3

DATABASE_NAME = "formula1.db"

def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.close()

if __name__ == "__main__":
    create_database()