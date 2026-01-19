#Write a program that takes a multiple user’s name and age as input and writes it to a file.
name = input("Enter your name: ")
age = input("Enter your age: ")
with open("user_info.csv", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

    