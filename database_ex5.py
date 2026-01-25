#Insert and retrieve employee records using Python.
import sqlite3
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                department TEXT
                )''')
employees = [
    (1, 'John Doe', 30, 'HR'),
    (2, 'Jane Smith', 25, 'IT'),
    (3, 'Mike Johnson', 35, 'Finance')
]
cursor.executemany("INSERT INTO employees VALUES(?, ?, ?, ?)", employees)
conn.commit()
cursor.execute("SELECT * FROM employees")
records = cursor.fetchall()
for record in records:
    print(record)
conn.close()