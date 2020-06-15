from functools import reduce

my_data = [1, 4, 6, 3, 17, 19, 25]
# [5, 6, 3, 17, 19, 25]
# [11, 3, 17, 19, 25]
# [14, 17, 19, 25]
pass
# my_data[0] = my_data[0] + my_data[1] -> len(my_data) == 1

result = reduce(lambda x, y: x + y, my_data)
# result = reduce(lambda x, y: x / y, my_data)
print(result)
