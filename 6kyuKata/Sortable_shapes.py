from math import pi


class Shape(object):
    def __lt__(self, other):
        return self.area < other.area


class Square(Shape):
    def __init__(self, side):
        self.area = side * side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.area = width * height


class Triangle(Shape):
    def __init__(self, base, height):
        self.area = base * height / 2.0


class Circle(Shape):
    def __init__(self, radius):
        self.area = radius ** 2 * pi


class CustomShape(Shape):
    def __init__(self, area):
        self.area = area

