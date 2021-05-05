number = int(input())
number_1 = ((number // 100) + (number // 10) % 10)
number_2 = (((number // 10) % 10) + (number % 100) % 10)
if number_1 > number_2:
    print(str(number_1) + str(number_2))
else:
    print(str(number_2) + str(number_1))