# Write a program that takes two numbers and handles division by zero.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Invalid Input: Please enter numerical values!")

#Output :
#Enter first number: 23
#Enter second number: 0
#Error: Division by zero is not allowed.