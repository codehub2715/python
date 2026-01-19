#Create a class Vehicle with a method start(). Inherit it in a class Car and override start().

class Vehicale:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicale):
    def start(self):
        print("Car is starting with a roar")
        
my_car = Car()
my_car.start()

