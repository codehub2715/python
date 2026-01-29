#Features:
#- Add, view, delete tasks
#- Store data in a text file

#add a task
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

#view tasks
def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())

#delete a task
def delete_task(task):
    with open ("tasks.txt", "r") as file:
        lines = file.readlines()
    with open("tasks.txt", "w") as file:
        for line in lines:
            if line.strip() != task:
                file.write(line)

while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task = input("Enter the task to delete: ")
        delete_task(task)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

