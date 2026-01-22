#Create a class Car with a class variable wheels = 4 and instance variable model.
class Car:
    wheels = 4
    def __init__(self,model):
        self.model=model

    def display(self):
        print("Model:",self.model)
        print("Wheels:",Car.wheels)

car1 = Car("Toyota")
car2 = Car("Honda")

car1.display()
car2.display()