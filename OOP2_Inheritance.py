#Inheritance allows one class (child) to inherit attributes and methods from another class (parent).

class Animal :
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
my_dog=Dog()

my_dog.sound()
my_dog.bark()
    