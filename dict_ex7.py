#Use pop() to remove an element and print the remaining dictionary.
Car = {'brand' : 'Hyundai','model' : 'Creta','year' : 2020}
removed_value = Car.pop('model')
print("Removed Value:", removed_value)
print("Remaining Dictionary:", Car)

#Output:
#Removed Value: Creta
#Remaining Dictionary: {'brand': 'Hyundai', 'year': 2020}
