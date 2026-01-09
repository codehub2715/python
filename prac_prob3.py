#Take a number from user and check:
#- Divisible by 3 and 5 → 'FizzBuzz'
#- Only by 3 → 'Fizz'
#- Only by 5 → 'Buzz'
#- Else → print the number

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# Sample Output :
#Enter a number: 20
#buzz
#Enter a number: 9
#Fizz
#Enter a number: 45
#FizzBuzz
#Enter a number: 7
#7

