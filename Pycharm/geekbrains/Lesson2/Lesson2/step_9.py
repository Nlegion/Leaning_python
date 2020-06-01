my_data = ['15', '196', '36', '473', '28', '74', '8']

# .append()
# my_data.pop()
last_el = my_data.pop()
print(my_data)
print(last_el)

last_el = my_data.pop(0)  # bad -> dequeue
print(my_data)
print(last_el)

