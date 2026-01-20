#Create a class Parent with a greet() method. Override greet() in a class Child using super().
class Parent:
    def greet(self):
        print("Parent!")

class Child(Parent):
    def greet(self):
        super().greet() 
        print("Child!")
        
parent = Parent()
parent.greet()  

child = Child()
child.greet()  
