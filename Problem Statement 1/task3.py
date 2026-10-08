import os
import csv
import sqlite3
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(base_dir, "users.csv")
db_name = os.path.join(base_dir, "users.db")

try:
    file = open(file_name, "r", newline="", encoding="utf-8")
    reader = csv.DictReader(file)

    if "name" not in reader.fieldnames or "email" not in reader.fieldnames:
        print("CSV file must contain name and email columns.")
    else:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)

        added = 0

        for user in reader:
            name = user.get("name", "").strip()
            email = user.get("email", "").strip()

            if not name or not email:
                continue

            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                continue

            cursor.execute(
                """
                INSERT OR IGNORE INTO users (name, email)
                VALUES (?, ?)
                """,
                (name, email)
            )

            if cursor.rowcount == 1:
                added += 1

        conn.commit()
        file.close()

        print("Users added:", added)

        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()

        print("\nUsers in database")
        print("-" * 45)

        for user in users:
            print("ID:", user[0])
            print("Name:", user[1])
            print("Email:", user[2])
            print("-" * 45)

        conn.close()

except FileNotFoundError:
    print("CSV file not found:", file_name)

except sqlite3.Error as error:
    print("Database error:", error)

except csv.Error as error:
    print("CSV file error:", error)