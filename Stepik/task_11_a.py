a = [int(input())]
x = 0
for i in a:
    if sum(a) != 0:
        a.append(int(input()))
    else:
        for q in a:
            q *= q
            x += q
print(x)
