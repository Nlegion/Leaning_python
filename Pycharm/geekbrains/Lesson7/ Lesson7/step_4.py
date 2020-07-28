from math import pi


class Circle:
    def __init__(self, r):
        self._r = r
        # self._area = pi * self._r ** 2  # 1 000 000 -> self._area 20
        self._area = None

    def get_area(self):
        self._area = pi * self._r ** 2
        return self._area

    def __str__(self):
        return f'{self.__class__.__name__}: {self._area}'


class Box:
    def __init__(self, w, h):
        self._w = w
        self._h = h
        # self._area = self._w * self._h
        self._area = None

    def get_area(self):
        self._area = self._w * self._h
        return self._area

    def __str__(self):
        return f'{self.__class__.__name__}: {self._area}'


circle_1 = Circle(r=15)
print(circle_1.get_area())
print(circle_1)

box_1 = Box(w=20, h=30)
print(box_1)
print(box_1.get_area())
