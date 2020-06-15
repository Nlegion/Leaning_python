import psutil
import time

start_memory = psutil.virtual_memory()[3]
start_time = time.perf_counter()
# print(start_memory)

max_number = 10 ** 6
# numbers = []
# for num in range(max_number):
#     numbers.append(num)


# numbers = (num for num in range(max_number))  # generator expression
# numbers = list((num for num in range(max_number)))  # generator expression -> list
# numbers = tuple((num for num in range(max_number)))  # generator expression -> list
# numbers = [num for num in range(max_number)]  # list generator
numbers = [num for num in range(max_number) if not num % 2]  # list generator

# numbers = []
# for num in range(max_number):
#     if not num % 2:
#         numbers.append(num)


result = sum(numbers)
print(result)  # 499999500000
print(type(numbers))


finish_memory = psutil.virtual_memory()[3]
finish_time = time.perf_counter()

memory_diff = (finish_memory - start_memory) / 2 ** 20
time_diff = (finish_time - start_time)
print(f'memory consumption {memory_diff:.3f} Mb, time {time_diff} s')
# memory consumption 41 Mb, time 0.1117939 s
