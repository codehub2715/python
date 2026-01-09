#Given a list of numbers, print only the even numbers.

numbers = [10, 15, 20, 30, 43, 55, 60]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("List of even numbers:", even_numbers)

#Output
#List of even numbers: [10, 20, 30, 60]