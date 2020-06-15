PI = 3.1415
calls_cnt = 0


def calc_circle_area(r):
    # r - local
    # PI - global
    # PI = 3.1415
    # PI - local
    # global PI
    # PI = 3.14
    global calls_cnt
    calls_cnt += 1
    return PI * r ** 2


radius = 5
print(PI, calls_cnt)
print(f'площадь окружности {calc_circle_area(radius):.2f}')
print(PI, calls_cnt)
print(f'площадь окружности {calc_circle_area(radius):.2f}')
print(PI, calls_cnt)
