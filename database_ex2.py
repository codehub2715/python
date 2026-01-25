# Write Python code to insert 3 records and display them.
import sqlite3
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER,
               grade TEXT
               )''')
students= [
    (1, 'Mayur', 21, 'A'),
    (2, 'Kirtan', 22, 'B'),
    (3, 'Alice', 20, 'A')
]
cursor.executemany("INSERT INTO students VALUES(?, ?, ?, ?)", students)
conn.commit()
conn.close()
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()
for record in records:
    print(record)
