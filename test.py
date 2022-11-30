from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return "вы создали квадрат"

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

class Rectangle:
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height

    def area(self):
        return self.widht * self.height

    def perimeter(self):
        return 2 * (self.widht + self.height)


def print_shape_info(shape):
    print(f"Area = {shape.area()}, perim = {shape.perimeter()}")

square = Square(10)
print_shape_info(square)
circle = Circle(10)
print_shape_info(circle)
rect = Rectangle(10, 15)
print_shape_info(rect)
print(square)