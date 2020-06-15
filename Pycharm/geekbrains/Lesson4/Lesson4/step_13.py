import psutil
import time

start_memory = psutil.virtual_memory()[3]
start_time = time.perf_counter()

max_number = 100
# numbers = {num: num ** 2 for num in range(max_number)}
numbers = {num for num in range(max_number)}

print(numbers)
print(type(numbers))

finish_memory = psutil.virtual_memory()[3]
finish_time = time.perf_counter()

memory_diff = (finish_memory - start_memory) / 2 ** 20
time_diff = (finish_time - start_time)
print(f'memory consumption {memory_diff:.3f} Mb, time {time_diff} s')
# memory consumption 41 Mb, time 0.1117939 s
