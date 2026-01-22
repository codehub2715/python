#Explore what happens when you override a class variable at the instance level.
class Car:
    wheels = 4

    def __init__(self, model):
        self.model = model

    def display(self):
        print("Model:", self.model)
        print("Wheels:", Car.wheels)

car1 = Car("Toyota")
car2 = Car("Honda")

car1.display()
car2.display()

Car.wheels = 6
car1.display()

Car.wheels = 8
car2.display()