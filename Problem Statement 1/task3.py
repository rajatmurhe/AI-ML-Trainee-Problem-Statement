import csv
import sqlite3

file_name = "users.csv"

try:
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT
                )
            """)

            for row in reader:
                name = row.get("name", "")
                email = row.get("email", "")
                cursor.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (name, email)
                )

            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()

            print("Users stored in database:")
            for user in users:
                print(user)

except FileNotFoundError:
    print("users.csv file not found.")

except sqlite3.Error as error:
    print("Database error:", error)