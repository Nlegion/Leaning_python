PI = 3.1415
pi = 3.1


def show_circle_area(r):
    area = PI * r ** 2
    print(f'площадь окружности радиуса {r} равна {area:.2f}')


# print(__name__)
if __name__ == '__main__':
    radius = 5
    show_circle_area(radius)

    radius = 15
    show_circle_area(radius)

    radius = 25
    show_circle_area(radius)
