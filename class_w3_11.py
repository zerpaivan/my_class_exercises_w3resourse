# Write a Python class named Circle constructed by a radius and two methods
# which will compute the area and the perimeter of a circle

from math import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


circle1 = Circle(10)
print(f"area circulo: {circle1.area():.2f}")
print(f"perimetro: {circle1.perimeter():.2f}")
