PI = 3.1415


def show_circle_area(radius, area):
    print(f'площадь окружности радиуса {radius} равна {area:.2f}')


def show_circle_area_2(area):
    print(f'площадь круга равна {area:.2f}')



def calc_circle_area(r):
    return PI * r ** 2


radius = 5
show_circle_area(radius, calc_circle_area(radius))

radius = 15
show_circle_area(radius, calc_circle_area(radius))

radius = 25
area = calc_circle_area(radius)
show_circle_area(radius, area)
show_circle_area_2(area)

# print(f'площадь круга равна {calc_circle_area(radius):.2f}')
# площадь круга равна

# 7 min -> 20:10
