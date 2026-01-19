#Build a command-line calculator using functions.

#Features:
#- Takes two numbers from user
#- Supports addition, subtraction, multiplication, division
#- Repeat until user exits

def add(x,y) : return x+y
def substract(x,y) : return x-y
def multiply(x,y) : return x*y
def divide(x,y) : return x/y

while True:
        print("Select Operation:")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        choice = input("Enter Operation (1/2/3/4 or 5): ")
        if choice == '5': break
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1': print(add(x,y))
        elif choice == '2': print(substract(x,y))
        elif choice == '3': print(multiply(x,y))
        elif choice == '4': print(divide(x,y))
        else: print("Invalid Input")