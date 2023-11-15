import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def main():
    circle = Circle(5)
    print("ARIA CERCULUI:", circle.area())
    print("PERIMETRUL CERCULUI:", circle.perimeter())

    rectangle = Rectangle(4, 6)
    print("ARIA DREPTUNGHIULUI:", rectangle.area())
    print("PERIMETRUL DREPTUNGHIULUI:", rectangle.perimeter())

    triangle = Triangle(3, 4, 5)
    print("ARIA TRIUNGHIULUI:", triangle.area())
    print("PERIMETRUL TRIUNGHIULUI:", triangle.perimeter())


main()
