#Create two classes Bird and Fish with a method move(). Demonstrate polymorphism using a loop.
class Bird:
    def move(self):
        print("The bird is flying.")

class Fish:
    def move(self):
        print("The fish is swimming.")

Animal = [Bird(), Fish()]

for obj in Animal:
    obj.move()

#Output:
#The bird is flying.
#The fish is swimming.