s = [int (i) for i in input ().split()]
l = len(s)-1
x = 0
for j in range (0,l+1):
    x = x + s[j]
print (x)
