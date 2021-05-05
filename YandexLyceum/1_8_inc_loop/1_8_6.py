credit = int(input())
livestock = int(input())
for b in range(1, credit // 20 + 1):
    for k in range((credit - b * 20) // 10 + 1):
        t = livestock - b - k
        if b * 20 + k * 10 + t * 5 == credit:
            print(b, k, t)
