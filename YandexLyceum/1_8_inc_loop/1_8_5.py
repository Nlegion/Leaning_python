a = int(input())
k = 0
for i in range(1, a):
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
    if k == 2:
        print(i)
    k = 0
