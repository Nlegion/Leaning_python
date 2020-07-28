import math


def normal_matrix_width(mat_1, mat_2):
    for item in range(int(math.fabs(len(mat_1[0]) - len(mat_2[0])))):
        for item2 in mat_1:
            item2.append(0)
    return mat_1


def normal_matrix_height(mat_1, mat_2):
    for item in range(int(math.fabs(len(mat_1) - len(mat_2)))):
        mat_1.append([0 for item2 in range(len(mat_1[0]))])
    return mat_1


class CalcM:

    def __init__(self, matrix):
        self.matrix = matrix

    def normal_matrix(self, other):
        if len(self.matrix) >= len(other.matrix):  # проверка на количество строк
            other.matrix = normal_matrix_height(other.matrix, self.matrix)
        elif len(self.matrix) <= len(other.matrix):
            self.matrix = normal_matrix_height(self.matrix, other.matrix)

        if len(self.matrix[0]) >= len(other.matrix[0]):  # проверка на количество столбцов
            other.matrix = normal_matrix_width(other.matrix, self.matrix)
        elif len(self.matrix[0]) <= len(other.matrix[0]):
            self.matrix = normal_matrix_width(self.matrix, other.matrix)

    def __add__(self, other):
        self.normal_matrix(other)
        return CalcM(
            [([self.matrix[item][item2] + other.matrix[item][item2] for item2 in range(len(self.matrix[item]))]) for
             item in range(len(self.matrix))])

    def __str__(self):
        return f"Матрица ({self.matrix})"


matrix_1 = CalcM([[31, 22], [37, 43], [51, 86]])
matrix_2 = CalcM([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = CalcM([[3, 5, 8, 3], [8, 3, 7, 1]])

print(matrix_1 + matrix_2)
print(matrix_2 + matrix_3)
print((matrix_1 + matrix_2) + matrix_3)