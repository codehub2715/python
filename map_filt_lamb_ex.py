#Create a pipeline using map, filter, and lambda to:
#- square numbers
#- filter out odd results
#- then sum them with reduce
#Example input: [1, 2, 3, 4, 5]
#Expected output: 20

from functools import reduce
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))

even_squares = list(filter(lambda x: x % 2 == 0, squared))
print("Even Squares:", even_squares)

result = reduce(lambda x, y: x + y, even_squares)
print("Final Result:", result)

#Output:
#Even Squares: [4, 16]
#Final Result: 20
