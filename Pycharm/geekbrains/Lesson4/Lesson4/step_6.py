import random

# num = 0
# while num < 10:
#     print(num)
#     num += 1

# for num in range(10):  # [0, 10)
#     print(num)

# for num in range(0, 10, 1):  # [0, 10)
# for num in range(1, 10 + 1, 2):  # [1, 10)
# for num in range(1, 10 + 1, 3):  # [1, 10)
#     print(num)

pass
# random.seed()
print(random.randrange(1, 10))  # [1, 10)
print(random.randrange(1, 10, 2))  # [1, 10)
print(random.randint(1, 10))  # [1, 10]
print(random.random())  # [0, 1)

start = 5
end = 15  # [5, 15)
print(start + random.random() * (end - start))
