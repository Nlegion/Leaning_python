# Разработать генератор случайных чисел.
# В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
# Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.

import random


def gen(start, finish):
    lis = []
    voc = {}
    if (start or finish) == 0:
        return 'Ноль нельзя'
    else:
        for _ in range(finish - start):
            rnd = random.randint(start, finish)
            lis.append(rnd)
            voc.update({'elem_{}'.format(rnd): rnd})
        return (lis, voc)


print(gen(7, 26))
