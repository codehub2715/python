#Given a list of numbers, use map() with lambda to get their cubes.
numbers = [1,2,3,4,5]
cubes = list(map(lambda x : x**3,numbers))
print("Cubes of numbers are:", cubes)

#Output:
#Cubes of numbers are: [1, 8, 27, 64, 125]
