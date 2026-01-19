#Use try-except-else-finally to read a file and print its contents.
try :
    with open("names.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found..")
else:
    print("File Content:\n", content)
finally:
    print("Execution completed.")