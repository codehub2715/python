# Use get() to access a key that doesn't exist.Provide a default value.
Car = {'brand' : 'Hyundai','model' : 'Creta','year' : 2020}
print("Color:", Car.get('color'))

print("Color with default:", Car.get('color', 'Not Specified'))
