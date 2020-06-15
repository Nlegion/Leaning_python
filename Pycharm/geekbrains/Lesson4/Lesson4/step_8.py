import psutil
import time

start_memory = psutil.virtual_memory()[3]
start_time = time.perf_counter()
# print(start_memory)

numbers = []
max_number = 10 ** 6
for num in range(max_number):
    numbers.append(num)

result = sum(numbers)
print(result)  # 499999500000

finish_memory = psutil.virtual_memory()[3]
finish_time = time.perf_counter()

memory_diff = (finish_memory - start_memory) // 2 ** 20
time_diff = (finish_time - start_time)
print(f'memory consumption {memory_diff} Mb, time {time_diff} s')
# memory consumption 41 Mb, time 0.1117939 s
