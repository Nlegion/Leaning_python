from sys import getsizeof

MAX_NUM = 10  # константа
nums = [num for num in range(1, MAX_NUM + 1)] #списочные включения
print(type(nums),getsizeof(nums))

nums_2 = (num for num in range(1, MAX_NUM + 1)) #генератор
print(type(nums_2),getsizeof(nums_2))

#разная алгоритмическая сложность nums - O(n), nums_2 - O(1)

