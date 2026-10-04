import requests
import sqlite3

url = "https://openlibrary.org/search.json"

search = input("Enter book name or topic: ")

try:
    response = requests.get(
        url,
        params={"q": search, "limit": 10},
        timeout=10
    )

    if response.status_code != 200:
        print("Unable to get books from the API.")
    else:
        data = response.json()
        books = data.get("docs", [])

        print("Books found:", len(books))

        with sqlite3.connect("books.db") as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT,
                    year INTEGER,
                    UNIQUE(title, author)
                )
            """)

            inserted = 0

            for book in books:
                title = book.get("title")

                if not title:
                    continue

                author_data = book.get("author_name", [])
                author = author_data[0] if author_data else "Unknown"
                year = book.get("first_publish_year")

                cursor.execute(
                    """
                    INSERT OR IGNORE INTO books
                    (title, author, year)
                    VALUES (?, ?, ?)
                    """,
                    (title, author, year)
                )

                if cursor.rowcount == 1:
                    inserted += 1

            print("New books added:", inserted)

            cursor.execute("""
                SELECT id, title, author, year
                FROM books
                ORDER BY id
            """)

            saved_books = cursor.fetchall()

        print("\nBooks stored in database")
        print("-" * 50)

        for book in saved_books:
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Year:", book[3] if book[3] else "N/A")
            print()

except requests.RequestException as error:
    print("Error while connecting to the API:", error)

except ValueError:
    print("Could not read the API response.")