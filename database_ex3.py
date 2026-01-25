#Update one record and delete another.
import sqlite3
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute("UPDATE students SET grade = ? WHERE id = ?", ('A+', 2))
cursor.execute("DELETE FROM students WHERE id = ?", (3,))
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()
for record in records:
    print(record)
conn.commit()
conn.close()
