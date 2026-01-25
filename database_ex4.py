import mysql.connector

try:
    # Connect to database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mayur2715",
        database="employeesDB"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, age) VALUES (%s, %s)",
        ("Mayur", 21)
    )
    conn.commit()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nEmployees Table Data:")
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print("Database error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
