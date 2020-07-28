from math import pi


class Figure:
    def __init__(self):
        self._area = None

    def get_area(self):
        if self._area is None:
            self._calc_area()
        return self._area

    def _calc_area(self):
        pass


class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self._r = r

    def _calc_area(self):
        print('call _calc_area')
        self._area = pi * self._r ** 2


class Box(Figure):
    def __init__(self, w, h):
        super().__init__()
        self._w = w
        self._h = h

    def _calc_area(self):
        print('call _calc_area')
        self._area = self._w * self._h


circle_1 = Circle(r=15)
print(circle_1.get_area())
print(circle_1.get_area())
print(circle_1.get_area())

box_1 = Box(w=20, h=30)
# print(box_1.get_area())
# 7 min -> 20:11 AIR
