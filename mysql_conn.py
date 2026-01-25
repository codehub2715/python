#Then connect to a MySQL server:
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mayur2715',
    database='school'
)
cursor = conn.cursor()

cursor.execute("SELECT DATABASE()")
print(cursor.fetchone())