import random


def next_from_bag(min_num=1, max_num=99):
    numbers = set()  # get() -> O(1), list -> O(n)
    while True:
        num = random.randint(min_num, max_num)
        while num in numbers:
            num = random.randint(min_num, max_num)
        numbers.add(num)
        if len(numbers) >= max_num - min_num + 1:
            break
        yield num
        # return num


my_numbers = next_from_bag()
print(type(my_numbers))
for _ in range(15):
    print(next(my_numbers))
