PI = 3.1415


# def show_circle_area(area, radius=None):
# def show_circle_area(*args):
def show_circle_area(*asdfasddsd, **sgsdfsadfsdefsdf):
    print(asdfasddsd)
    print(sgsdfsadfsdefsdf)
    pass

# def show_circle_area(*asdfasddsd, **sgsdfsadfsdefsdf):
#     if radius is not None:
#         print(f'площадь окружности радиуса {radius} равна {area:.2f}')
#     else:
#         print(f'площадь круга равна {area:.2f}')


def calc_circle_area(r):
    return PI * r ** 2


radius = 5
area = calc_circle_area(radius)


# max()
show_circle_area(area, radius, area, radius)
show_circle_area(area, radius)
show_circle_area(area)
show_circle_area()

show_circle_area(area=area, radius=radius, radius_2=radius, area_2=area)
