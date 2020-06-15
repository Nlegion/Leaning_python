# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func_1(a, b, c):  # классический вариант
    z = 0
    if a > b:
        if c > b:
            z = a + c
        else:
            z = a + b
    else:
        if c > a:
            z = b + c
    return z


def my_func(*args):  # новый вариант
    z = sorted(args)
    z.reverse()
    z.pop()
    return sum(z)


a = 4
b = 2
c = 3

print(my_func(a, b, c))
print(my_func_1(a, b, c))
