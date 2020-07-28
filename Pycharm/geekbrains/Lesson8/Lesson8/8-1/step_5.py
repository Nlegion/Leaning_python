class Matrix:

    def __init__(self, m_list):
        self._m_list = m_list

    @staticmethod
    def create_and_validate(m_list):
        Matrix.is_valid(m_list)
        return Matrix(m_list)

    @staticmethod
    def is_valid(data):
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


class SquareMatrix(Matrix):
    pass

    @staticmethod
    def create_and_validate(m_list):
        SquareMatrix.is_valid(m_list)
        return SquareMatrix(m_list)


try:
    a = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])

    # b = Matrix([
    #     [10, 20, 10],
    #     [40, 50, 80],
    # ])

    # b = Matrix.create_and_validate([
    #     [10, 20, 10],
    #     [40, 50, 80],
    # ])

    # b = SquareMatrix([
    #     [10, 20, 10],
    #     [40, 50, 80],
    # ])

    b = SquareMatrix.create_and_validate([
        [10, 20, 10],
        [40, 50, 80],
    ])

    print(type(b))

    d = a + b
    print(d)

except ValueError as e:
    # print(f'видимо, разные размеры: {e}')
    print(f'неверные данные: {e}')
except AttributeError as e:
    print(e)
except Exception as e:
    print(e)
