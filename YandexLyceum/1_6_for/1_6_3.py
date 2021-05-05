number = int(input())
dividers = []
for i in range(1, number + 1):
    if number % i == 0:
        dividers.append(i)
        print(i, end=' ')
print('ПРОСТОЕ' if len(dividers) == 2 else 'НЕТ')

