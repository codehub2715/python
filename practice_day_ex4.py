#Build a lambda function that multiplies two numbers and use it with map() to apply it on a list of tuples.
two_numbers = [(1,2), (4,5), (10,20), (50,60)]
multiply = lambda x : x[0] * x[1]
result = list(map(multiply, two_numbers))

print("Multiplies two numbers : " ,result)

#Output:
#Multiplies two numbers :  [2, 20, 200, 3000]
