# Append a new name to the same file without deleting existing content.
with open("names.txt", "a") as file:
    file.write("Kirtan\n")
    file.write("Raj\n")
    