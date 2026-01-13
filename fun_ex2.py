#Write a function that checks if a number is even or odd.
def even_odd(number):
    if number %2==0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter the number: "))
print("Number is",even_odd(num))
