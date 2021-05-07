basket = ['159.5', '789.2', '647.7']

basket_as_int = []  # базовый пример
for item in basket:
    basket_as_int.append(int(float(item)))
print(basket_as_int)

# пример лямбды
add = lambda x, y: x * y  # параметры : действие
print(add(float(basket[0]), float(basket[1])))

# map применяет первый параметр к остальным
basket_as_int_map = map(int, map(float, basket))  # map итератор
print(*basket_as_int_map, sum(basket_as_int_map))  # * - распаковка итератора

basket_as_int_filter = filter(lambda x: x > 500,
                              map(int, map(float, basket)))
print(sum(basket_as_int_filter))

print(list(
    filter(
        lambda x: x % 2 == 0,
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))  # только четные

# zip итератор объединения по наименьшей последовательности
a = [5, 6, 7]
b = [1, 2, 3, 4]
print(list(zip(a, b)))
