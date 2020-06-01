my_data = ['15', '196', '36', '473', '28', ['74']]
# my_data_3 = my_data
my_data_3 = my_data.copy()  # shallow
# deepcopy

print(id(my_data), id(my_data_3))
print(id(my_data) == id(my_data_3))
print(my_data is my_data_3)


my_data_3[0] = True
print(my_data)
print(my_data_3)

# 7 min -> 20:12 AIR
