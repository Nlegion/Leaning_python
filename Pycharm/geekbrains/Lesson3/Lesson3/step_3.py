PI = 3.1415


# def calc_circle_area(r):
#     _area = PI * r ** 2  # r - exists only inside of the func
#     return _area


def calc_circle_area(r):
    return PI * r ** 2


radius = 5
area = calc_circle_area(radius)  # call the func
print(f'площадь окружности радиуса {radius} равна {area:.2f}')

radius = 15
print(f'площадь окружности радиуса {radius} равна {calc_circle_area(radius):.2f}')

radius = 25
print(f'площадь окружности радиуса {radius} равна {calc_circle_area(radius):.2f}')

print(f'площадь окружности равна {calc_circle_area(100):.2f}')
