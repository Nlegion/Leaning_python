n = int(input())
a = []
i = 0
s = "ABCDEFGHI"
if n < 10:
    for i in range(n):
        m = n
        m = m - i
        for j in range(n):
            print(s[j] + str(m), end=' ')
        print()