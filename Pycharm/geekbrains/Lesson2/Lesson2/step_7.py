# import timeit

my_data = ['15', '196', '36', '473', '28', '74', '8']

# idx = 0
# result = 0
# while idx < len(my_data):  # bad :(
#     result += int(my_data[idx])
#     idx += 1
#
# print(result)  # 830

result = 0
for item in my_data:  # good
    result += int(item)
print(result)  # 830
