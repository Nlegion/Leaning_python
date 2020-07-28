#  Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
#  которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм.
#  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#  Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Material:
    def __init__(self, param_v, param_h):
        self.param_v = param_v
        self.param_h = param_h

    def coat(self):
        square_c = self.param_v / 6.5 + 0.5
        return square_c

    def suit(self):
        square_s = self.param_h * 2 + 0.3
        return square_s

    @property
    def my_method(self):
        return f'Общая площадь ткани: {round(self.suit() + self.coat())} = на костюмы {round(self.suit(), 1)} + на пальто {round(self.coat(), 1)} '


class Coat(Material):
    def __init__(self, param_v, param_h):
        super().__init__(param_v, param_h)
        self.square_c = self.param_v / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто {round(self.square_c,1)}'


class Suit(Material):
    def __init__(self, param_v, param_h):
        super().__init__(param_v, param_h)
        self.square_s = self.param_h * 2 + 0.3

    def __str__(self):
        return f'Площадь на костюм {round(self.square_s,1)}'


mc = Material(12, 4)
coat = Coat(12, 0)
suit = Suit(0, 4)

print(mc.my_method)
print(coat)
print(suit)
