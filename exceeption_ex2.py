#Accept a string from the user and convert it to integer with proper exception handling.
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print("Input a number is:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

#Output :
#Enter a number: abc
#Invalid input! Please enter a valid integer.