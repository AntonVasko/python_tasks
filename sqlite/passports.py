import sqlite3

conn = sqlite3.connect("passports.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL           
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS passports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        number TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)           
    )
""")

cursor.execute("INSERT INTO users (name) VALUES ('Олег')")
cursor.execute("INSERT INTO passports (user_id, number) VALUES (1, '12131')")
conn.commit()
conn.close()