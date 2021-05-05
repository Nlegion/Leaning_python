from itertools import combinations

n = int(input())
a = [int(input()) for _ in range(n)]
p = int(input())

flag = any(p == a * b for a, b in combinations(a, 2))
print("ДА" if flag else "НЕТ")
