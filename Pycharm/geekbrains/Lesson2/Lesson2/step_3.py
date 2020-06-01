import sys

my_data = ['15', '196', '36', '473', '28', '74']
my_data_2 = ('15', '196', '36', '473', '28', '74')
# print(type(my_data), type(my_data_2))
# print(sys.getsizeof(my_data), sys.getsizeof(my_data_2))
# object mutable (in place) VS immutable

my_data[0] = True  # mutable
print(my_data)

# my_data_2[0] = True  # immutable
# print(my_data_2)  # reverse() ?

print(dir(my_data_2))
