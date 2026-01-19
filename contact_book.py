#Build a basic contact book using dictionaries and file handling.

#Features:
#- Add new contact (name, phone)
#- Search contact by name
#- Save contacts to file and load on startup



contacts = {}
try:
    with open("contacts.txt", "r") as f:
        for line in f:
            name, phone = line.strip().split(',')
            contacts[name] = phone
except FileNotFoundError:
    pass
    
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        with open("contacts.txt", "a") as f:
            f.write(f"{name},{phone}\n")
        print("Contact added.")
        
    elif choice == '2':
        name = input("Enter name to search: ")
        print("Found:", contacts.get(name, "Not Found"))
    elif choice == '3':
        break



