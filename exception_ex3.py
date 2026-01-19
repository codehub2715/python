#Create a function that only accepts integers between 1 and 100. Raise an error if not.
def accept_integer(num):
    if num <1 or num>100:
        raise ValueError("Number must be between 1 and 100.")
    return num
try : 
    user_input = int(input("Enter an integer between 1 and 100: "))
    valid_number = accept_integer(user_input)
    print("You entered a valid number:", valid_number)
except ValueError: print("Invalid input! Please enter an integer between 1 and 100.")
