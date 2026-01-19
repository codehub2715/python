#Create a mini program that handles different types of errors like IndexError, ValueError, and FileNotFoundError.

try:
    my_list = [22,44,77,543]
    print(my_list[6]) 
except IndexError:
    print("IndexError occured")
try:
    num = int(input("Input a number : "))
except ValueError:
    print("ValueError occured")
try:
    with open("abc.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("FileNotFoundError occured")