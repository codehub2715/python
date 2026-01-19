#Define a class Circle with a radius attribute and a method to calculate area.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
circle1 = Circle(2)
print("Area of the circle:", circle1.area())
