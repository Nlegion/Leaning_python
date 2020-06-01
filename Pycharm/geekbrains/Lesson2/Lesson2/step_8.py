# to int, IN PLACE, !!!change iterable!!!
my_data = ['15', '196', '36', '473', '28', '74', '8']

# print(my_data)
# idx = 0
# while idx < len(my_data):
#     my_data[idx] = int(my_data[idx])
#     idx += 1
#
# result = sum(my_data)
# print(result)


result = 0
for item in my_data:  # n -> range()
    item = int(item)
    # my_data.append(item)  # change iterable!!!
    # my_data[my_data.index(item)] = int(item)  # n
# n^2

print(my_data)
# enumerate()
