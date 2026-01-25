#Create a SQLite database with a table books (title, author, year).

import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
               title TEXT,
               author TEXT,
               year INTEGER
               )''')
conn.commit()
conn.close()
