n = int(input())
a = []
for i in range(n):
    f = input()
    if 'лук' in f:
        continue
    a.append(f)
print(', '.join(a))
