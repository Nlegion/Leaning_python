PI = 3.1415


def show_circle_area(area, radius=None):
    if radius is not None:
        print(f'площадь окружности радиуса {radius} равна {area:.2f}')
    else:
        print(f'площадь круга равна {area:.2f}')


def calc_circle_area(r):
    return PI * r ** 2


radius = 5
area = calc_circle_area(radius)

show_circle_area(area, radius)
show_circle_area(area)
