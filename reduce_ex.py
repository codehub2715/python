#Use reduce() to find the maximum number in a list.
from functools import reduce
numbers = [10,44,55,70,95,23]
maximum = reduce(lambda x,y: x if x>y else y,numbers)
print("Maximum number is:", maximum)

#Output:
#Maximum number is: 95
