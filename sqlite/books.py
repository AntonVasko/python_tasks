import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL           
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        book TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)           
    )
""")

cursor.execute("INSERT INTO users (name) VALUES ('Олег')")
cursor.execute("INSERT INTO books (user_id, book) VALUES (1, 'Книга 1')")
cursor.execute("INSERT INTO books (user_id, book) VALUES (1, 'Книга 2')")
conn.commit()
conn.close()