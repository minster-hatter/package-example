import math as m


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle, given the radius."""
        return m.pi * self.radius ** 2

    def circumf(self):
        """Calculate the circumference of a circle, given the radius."""
        return 2 * m.pi * self.radius


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        """Calculate the area of a square, given the length."""
        return self.length ** 2

    def perim(self):
        """Calculate the perimeter length of a square, given the length"""
        return 4 * self.length
