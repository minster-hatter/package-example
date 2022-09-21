import math as m

from foo import bar

u = 1

a_circle = bar.Circle(u)
a_square = bar.Square(u)


def test_circle():
    assert a_circle.area() == m.pi
    assert a_circle.circumf() == 2 * m.pi


def test_square():
    assert a_square.area() == u
    assert a_square.perim() == 4 * u
