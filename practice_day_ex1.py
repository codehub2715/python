#Create a function that accepts a list of numbers and returns a new list with only even numbers.
def filter_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Even Numbers:", even_numbers)

