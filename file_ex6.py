#Copy the contents of one file to another.
with open("names.txt","r") as file1:
    content = file1.read()
    with open("copy.txt","w") as file2:
        file2.write(content)