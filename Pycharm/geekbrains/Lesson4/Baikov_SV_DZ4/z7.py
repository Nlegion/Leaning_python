# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

import sys


# необходимо ввести № скрипта и его параметр

def generator(com):
    com = int(com)
    for el in range(1, com + 1):
        yield el


def generator_2(com):
    com = int(com)
    a = 0
    b = 1
    for el in range(1, com + 1):
        a, b = b, a + b
        yield a


# user_fac = sys.argv[1]
user_fac = 4
z = 1
y = 0

g = generator(user_fac)
for el in g:
    z *= el
print('Факториал числа {0} = {1}'.format(user_fac, z))

g2 = generator_2(user_fac)
for item in g2:
    y = item
print('{0} число фибоначчи = {1}'.format(user_fac, y))
