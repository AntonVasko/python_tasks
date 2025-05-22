import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL           
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL           
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id)
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")

with open('data.txt', 'r', encoding = 'utf-8') as f:
    files = f.readlines()
    names = files[0].rstrip('\n').split()
    courses = files[1].rstrip('\n').split()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())
cursor.execute("SELECT * FROM courses")
print(cursor.fetchall())
cursor.execute("SELECT * FROM student_courses")
print(cursor.fetchall())
data = input()
while data != '':
    typed, file = data.split()
    if typed.lower() == 'имя':
        cursor.execute(f"INSERT INTO students (name) VALUES ('{file}')")
        names.append(file)
    elif typed.lower() == 'курс':
        courses.append(file)
        cursor.execute(f"INSERT INTO courses (title) VALUES ('{file}')")
    else:
        cursor.execute(f"INSERT INTO student_courses VALUES ({typed}, {file})")
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM courses")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM student_courses")
    print(cursor.fetchall())
    conn.commit()
    data = input()
with open('data.txt', 'w', encoding = 'utf-8') as f:
    f.write(' '.join(names))
    f.write('\n')
    f.write(' '.join(courses))
    f.write('\n')

cursor.execute("SELECT * FROM student_courses")

for el in names:
    cursor.execute(f"SELECT id FROM students WHERE name = '{el}'")
    sid = str(cursor.fetchone()).lstrip('(').rstrip(',)')
    cursor.execute(f"SELECT course_id FROM student_courses WHERE student_id = {sid}")
    goes = list()
    for i in cursor.fetchall():
        i = str(i).lstrip('(').rstrip(',)')
        cursor.execute(f"SELECT title FROM courses WHERE id = {i}")
        goes.append(str(cursor.fetchone()).lstrip('(').rstrip(',)'))
    print(f"{el} ходит на такие курсы: {', '.join(goes)}")