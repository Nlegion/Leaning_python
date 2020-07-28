# a = 15
# b = 25
# d = 40
#
# c = a + b + d
# print(c)

from math import pi


class Figure:
    unit = 'm'

    def __init__(self):
        self._area = None
        self._calc_area()

    def get_area(self):
        return self._area

    def _calc_area(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: {self._area:.2f} {self.unit}^2'

    def __add__(self, other):
        # self._area + other._area
        # return self._area + other._area  # returns -> int()
        result = Figure()
        result._area = self._area + other._area
        return result  # return object same class!!!


class Circle(Figure):
    def __init__(self, r):
        self._r = r
        super().__init__()  # self._area = None

    def _calc_area(self):
        self._area = pi * self._r ** 2


class Box(Figure):
    def __init__(self, w, h):
        self._w = w
        self._h = h
        super().__init__()

    def _calc_area(self):
        self._area = self._w * self._h


circle_1 = Circle(r=15)
box_1 = Box(w=20, h=30)
box_2 = Box(w=50, h=70)

total_area = circle_1 + box_1 + box_2 + circle_1 + circle_1
# total_area = circle_1 + box_1
#           left oper   right oper
#                self   other
#                    int + box_2
#               Figure() + box_2 -> OK !!!!!!!!!!!!!!!!
print(total_area)

# 15 + circle_1

# __hash__
