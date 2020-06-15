import psutil
import time

start_memory = psutil.virtual_memory()[3]
start_time = time.perf_counter()
# print(start_memory)

max_number = 10 ** 6
# numbers = []
# for num in range(max_number):
#     numbers.append(num)


numbers = (num for num in range(max_number))  # generator expression


print(next(numbers))  # save state
print(next(numbers))  # save state
print(next(numbers))
print(next(numbers))
print(next(numbers))

result = sum(numbers)
print(result)  # 499999500000
# print(numbers[10001], numbers[100005])
# print(type(numbers))

print(next(numbers))

finish_memory = psutil.virtual_memory()[3]
finish_time = time.perf_counter()

memory_diff = (finish_memory - start_memory) / 2 ** 20
time_diff = (finish_time - start_time)
print(f'memory consumption {memory_diff:.3f} Mb, time {time_diff} s')
# memory consumption 41 Mb, time 0.1117939 s
