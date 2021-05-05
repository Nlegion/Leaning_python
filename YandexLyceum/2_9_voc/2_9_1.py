def coun(x):
    dct[x] = dct.get(x, 0) + 1
    return dct[x]


dct = {}
print(*[coun(k) for k in input().split()])
