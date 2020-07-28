# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:

    def __init__(self, m_list):
        self.is_valid(m_list)
        self._m_list = m_list

    def is_valid(self, data):
        # print(list(map(len, data)))
        if len(set(map(len, data))) != 1:
            raise ValueError('input list is not valid')

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self._m_list]))

    def m_print(self, i, j):
        print(self._m_list[i][j])

    def __add__(self, other):
        if not self.size == other.size:
            raise ValueError(
                f'matrix sizes differs: {self.size} != {other.size}'
            )

        return Matrix(
            [
                [
                    self._m_list[i][j] + other._m_list[i][j]
                    for j in range(len(self._m_list[0]))
                ]
                for i in range(len(other._m_list))
            ]
        )

    @property
    def size(self):
        return len(self._m_list), len(self._m_list[0])


try:
    a = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])
    b = Matrix([
        [10, 20, 10],
        [40, 50, 80],
        # [40, 50, 60],
        # [20, 5, 90],
    ])
    # c = Matrix([[10, 20, 30],
    #             [40, 50, 60]])
    # d = a + b + c
    d = a + b
    print(d)

except ValueError as e:
    # print(f'видимо, разные размеры: {e}')
    print(f'неверные данные: {e}')
except AttributeError as e:
    print(e)
except Exception as e:
    print(e)
