# Read the contents of the above file and print all names in uppercase.
file = open("names.txt", "r")
content = file.readlines()
for name in content:
    print(name.strip().upper())
    file.close()