from math import pi


class Figure:
    def __init__(self):
        self._area = None

    def get_area(self):
        return self._area


class Circle(Figure):
    def __init__(self, r):
        super().__init__()  # self._area = None
        self._r = r

    def calc_area(self):
        self._area = pi * self._r ** 2


class Box(Figure):
    def __init__(self, w, h):
        super().__init__()
        self._w = w
        self._h = h

    def calc_area(self):
        self._area = self._w * self._h


circle_1 = Circle(r=15)
circle_1.calc_area()
print(circle_1.get_area())

box_1 = Box(w=20, h=30)
box_1.calc_area()
print(box_1.get_area())

