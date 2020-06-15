PI = 3.1415


def show_circle_area(area, radius=None, *args, **kwargs):
    """Prints circle area in different ways"""

    units = kwargs.get('units')
    if len(args) > 0:
        units = args[0]

    if radius is not None:
        print(f'площадь окружности радиуса {radius} равна {area:.2f}', end='')
    else:
        print(f'площадь круга равна {area:.2f}', end='')
    if units:
        print(f' {units}^2')
    else:
        print()


def calc_circle_area(r):
    """Calcs area of circle

    :param r: raduis, int or float
    :return:
    """
    return PI * r ** 2


radius = 5
area = calc_circle_area(radius)

show_circle_area(area, radius)
show_circle_area(area)

show_circle_area(area, radius, 'см')
show_circle_area(area, radius, units='см')
show_circle_area(area, units='см')

# show_circle_area(area, radius, area, radius)
# show_circle_area(area, radius)
# show_circle_area(area)
# show_circle_area()
#
# show_circle_area(area=area, radius=radius, radius_2=radius, area_2=area)

help(show_circle_area)
