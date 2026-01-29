#Features:
#- Connect to SQLite
#- Perform Create, Read, Update, Delete operations
#Table: students(name, age, grade)

import sqlite3

conn = sqlite3.connect('student_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        grade TEXT
    )
''')

conn.close()

#CRUD operations
def create_student(name, age, grade):
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

def read_student(name):
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", (name,))
    student = cursor.fetchone()
    conn.close()
    return student

def update_student(name, age, grade):
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age=?, grade=? WHERE name=?", (age, grade, name))
    conn.commit()
    conn.close()

def delete_student(name):
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()
    conn.close()

while True:
    print("1. Create a student")
    print("2. Read a student")
    print("3. Update a student")
    print("4. Delete a student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        grade = input("Enter the grade: ")
        create_student(name, age, grade)

    elif choice == "2":
        name = input("Enter the name: ")
        student = read_student(name)
        if student:
            print("Name:", student[0])
            print("Age:", student[1])
            print("Grade:", student[2])
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        grade = input("Enter the grade: ")
        update_student(name, age, grade)

    elif choice == "4":
        name = input("Enter the name: ")
        delete_student(name)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")