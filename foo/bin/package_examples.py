from pathlib import Path

from foo import bar, baz

p = Path(__file__).parent / "../data/radius_length.txt"
print(p)
with open(p) as f:
    lines = f.readlines()

radius, length = int(lines[0][0]), int(lines[0][3])

a_circle = bar.Circle(radius)
a_square = bar.Square(length)

print(radius, length)
print("Circle area: ", a_circle.area())
print("Circle circumference: ", a_circle.circumf())

print("Square area: ", a_square.area())
print("Square perimeter: ", a_square.perim())

print("Baz Pythons: ", baz.pythons())
