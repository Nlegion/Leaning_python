from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    unit = 'm'

    def __init__(self):
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._calc_area()
        return self._area

    @abstractmethod
    def _calc_area(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: {self.area:.2f} {self.unit}^2'


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


class GeometryCollection:  # like Basket
    def __init__(self):
        self._figures = []

    def add(self, item):
        if isinstance(item, Figure):  # check
            self._figures.append(item)

    def remove(self, item):
        if self._figures.count(item) > 0:
            self._figures.remove(item)

    def get_total_area(self):
        return sum(el.area for el in self._figures)
        # return sum([el._area for el in self._figures])

    def __getitem__(self, item):
        # if item < len(self._figures):
        #     return self._figures[item]
        try:
            return self._figures[item]
        except Exception as e:
            print(e)


circle_1 = Circle(r=15)
circle_2 = Circle(r=5)
circle_3 = Circle(r=25)
box_1 = Box(w=20, h=30)
box_2 = Box(w=45, h=70)

shelf_1 = GeometryCollection()
shelf_1.add(circle_1)
shelf_1.add(box_2)
shelf_1.add(box_1)
shelf_1.add(circle_2)
shelf_1.add(circle_3)

# print(shelf_1.get_total_area())

print(shelf_1[0])
print(shelf_1[1])
