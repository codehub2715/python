import sqlite3
 
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary REAL
)
""")
 
cursor.execute("""
INSERT INTO employees (name, age, salary)
VALUES (?, ?, ?)
""", ("Karan", 27, 38000))
 
conn.commit()
 
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())
 
conn.close()