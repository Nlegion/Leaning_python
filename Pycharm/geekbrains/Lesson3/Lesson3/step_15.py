def change_it(x):
    return -int(x)


my_data = ['1', '2', '7', '0', '77', '3']

# my_data_as_str = list(map(change_it, my_data))
# my_data_as_str = list(map(lambda x: -int(x), my_data))
my_data_as_str = list(map(int, my_data))
# my_data_as_str = list(map(lambda z: int(z), my_data))
print(my_data_as_str)

# lambda x: -int(x)


# '15 5 8 9 11'
# '25 8 7 q 8 9'
# .title()  # no

# user_input = [
#     '15 5 8 9 11',
#     '15 5 8 9 11',
#     '25 8 7 q 8 9',
#     '15 5 8 9 11',
# ]
