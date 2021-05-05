a = (map(int, input().split()))
b = list(map(str.lower, input().split()))
print(' '.join([b[i - 1] for i in a]).capitalize())
