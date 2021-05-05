import numpy as np


def minutes(x):
    y = x.split(':')
    return int(y[0]) * 60 + int(y[1])


def late(now, classes, bus):
    bus_ar = np.array(bus)
    bus_time = 15
    walk_time = 5
    max_time = minutes(classes) - minutes(now) - bus_time
    t = -1
    for a in map(int, bus_ar):
        if a > max_time:
            break
        t = a
    t -= walk_time
    message = "Выйти через {0} минут".format(t) if t >= 0 else "Опоздание"
    return message