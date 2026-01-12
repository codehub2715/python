#Create a dictionary with keys: 'brand', 'model', 'year'. Print each value.
Car = {'brand' : 'Hyundai','model' : 'Creta','year' : 2020}

print("Brand:", Car['brand'])
print("Model:", Car['model'])
print("Year:", Car['year'])


# Add a new key 'color' to the dictionary and update the value of 'year'.
Car['Color'] = 'White'
Car['year'] = 2021
print("Updated Car Dictionary:", Car)

# Delete the key 'model' and print the updated dictionary.
del Car['model']
print("Updated Dictionary:", Car)


#Output:
#Brand: Hyundai
#Model: Creta
#Year: 2020
#Updated Car Dictionary: {'brand': 'Hyundai',
#'model': 'Creta', 'year': 2021, 'Color': 'White'}
#Updated Dictionary: {'brand': 'Hyundai', 'year': 2021, 'Color': 'White'}
