a = [0] * 30000
s = 15000
b = input()
for i in range(len(b)):
    if a[s] >= 256:
        a[s] = 0
    elif s == 30001:
        s = 15000
    elif b[i] == '>':
        s += 1
    elif b[i] == '+':
        a[s] += 1
        if a[s] == 256:
            a[s] = 0
    elif b[i] == '<':
        s -= 1
    elif b[i] == '.':
        print(a[s])
    elif b[i] == '-':
        if a[s] != 0:
            a[s] -= 1
        else:
            a[s] = 255
