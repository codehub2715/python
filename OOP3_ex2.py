#Create a class Product and override __str__ to return its name and price.
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f"{self.name} : {self.price}"

p1=product("Laptop",100000)
print(p1)

#Output:
#Laptop : 100000