PI = 3.1415


def calc_circle_area(r):
    # PI = 0  # local
    # print(PI)  # global
    # PI = PI  # local
    # PI += 1  # local
    return PI * r ** 2


radius = 5
print(f'площадь окружности {calc_circle_area(radius):.2f}')
