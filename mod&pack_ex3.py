#Create a custom module with a function that converts Celsius to Fahrenheit.

def celsTOfahen(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in celsius: "))
print(f"{celsius} degree Celsius is = {celsTOfahen(celsius)} degree Fahrenheit.")

#fahrenheit to celsius conversion
def fahenTOcelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = float(input("Enter temperature in fahrenheit: "))
print(f"{fahrenheit} degree Fahrenheit is = {fahenTOcelsius(fahrenheit)} degree Celsius.")
