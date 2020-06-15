# PI = 3.1415
#
#
# def show_circle_area(radius, area):
#     print(f'площадь окружности радиуса {radius} равна {area:.2f}')
#
#
# def calc_circle_area(r):
#     return PI * r ** 2
#
#
# radius = 5
# show_circle_area(radius, calc_circle_area(radius))  # () - call
#
# radius = 15
# show_circle_area(radius, calc_circle_area(radius))
# print(show_circle_area)  # as callback, no calculations and actions
# print(show_circle_area(1, 2))  # call, calculations and actions


def do_something(series, action):
    return action(series)
    # return max(series)
    # return min(series)


my_data = [1, 2, 7, 0, 77, 3]
print(do_something(my_data, max))
print(do_something(my_data, min))
print(do_something(my_data, sorted))

# my_data_as_str = list(map(str(), my_data))
my_data_as_str = list(map(str, my_data))
print(my_data_as_str)
