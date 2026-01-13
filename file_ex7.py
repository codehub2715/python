#Use with statement to read and write to files safely.
with open("example.txt", "w") as file:
    file.write("This is a statement1.\n")
    file.write("This is a statement2.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
    
        