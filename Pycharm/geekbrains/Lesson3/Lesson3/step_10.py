PI = 3.1415


def show_circle_area(radius, area):
    print(f'площадь окружности радиуса {radius} равна {area:.2f}')


def calc_circle_area(r):
    return PI * r ** 2


radius = 5
area = calc_circle_area(radius)

# my_positional_args = radius, area
my_positional_args = [radius, area]
show_circle_area(*my_positional_args)

show_circle_area(radius, area)  # positional, as list, args
# show_circle_area(area, radius)
#
show_circle_area(area=area, radius=radius)  # named, as dict, kwargs
show_circle_area(radius=radius, area=area)  # named, as dict, kwargs

my_named_args = {
    'radius': 155,
    'area': calc_circle_area(155)
}
show_circle_area(**my_named_args)


show_circle_area(radius, area=area)

print('hello', 'go', 'jump', sep=' | ')
# print(sep=' | ', 'hello', 'go', 'jump')
# print('hello', 'go', sep=' | ', 'jump')
