# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


import sys


def user_calc(watch, rate, premium):
    user_pay = (int(watch) * int(rate)) + int(premium)
    return user_pay


about_worker = sys.argv
# about_worker = 'z1','Ivan', 7, 500, 100
if len(about_worker) < 4:
    print('Мало аргументов')
else:
    if len(about_worker) >= 5:
        id, id_worker, watch, rate, premium, *other = about_worker
    elif len(about_worker) == 4:
        id, id_worker, watch, rate = about_worker
        premium = 0

    print('Сотрудник: {0} получит {1} денег'.format(id_worker, user_calc(watch, rate, premium)))


