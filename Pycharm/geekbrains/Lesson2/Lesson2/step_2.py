my_data = ['15', '196', '36', '473', '28', '74']
# 1 000 000 x 2
# print(dir(my_data))

# print(my_data.reverse())

# object -> attribute and method
# my_data.items -> attribute access
# my_data.get_items() -> call the method
my_data.reverse()  # in place -> no new List -> memory economy
print(my_data)

# print(my_data.append('47'))
my_data.append('47')
my_data.append('196')
print(my_data)

print(my_data.index('196'))
print(my_data.count('196'))
print(my_data.count('197'))
# print(my_data.index('197'))
