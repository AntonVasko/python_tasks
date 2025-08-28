import sqlite3
import json

conn = sqlite3.connect("cassa.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL           
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER,
        discount TEXT,
        discounted_price INTEGER,
        ammount INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS checks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        summ INTEGER,
        user_id INTEGER UNIQTE,
        FOREIGN KEY (user_id) REFERENCES users(id)            
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products_checks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        check_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (check_id) REFERENCES ckecks(id),
        FOREIGN KEY (product_id) REFERENCES products(id)           
    )
""")

with open('cassa.json') as f:
    data = json.load(f)
to_ins = []
for el in data:
    pr = data[el]
    to_ins.append((el, pr['Цена'], pr['Скидка'], pr['Цена со скидкой'], 15))

cursor.executemany('''
    INSERT INTO products(name, price, discount, discounted_price, ammount) VALUES (?, ?, ?, ?, ?)
''', to_ins)




cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
cursor.execute("SELECT * FROM products")
print(cursor.fetchall())
cursor.execute("SELECT * FROM checks")
print(cursor.fetchall())
cursor.execute("SELECT * FROM products_checks")
print(cursor.fetchall())
"""cursor.execute("SELECT ammount FROM products WHERE name == 'Молоко'")
ins = int(cursor.fetchone()[0]) - 1
cursor.execute(f'''INSERT INTO products(ammount) VALUES (1)''')
cursor.execute("SELECT ammount FROM products WHERE name == 'Молоко'")
print(cursor.fetchone)"""
conn.commit()
conn.close()