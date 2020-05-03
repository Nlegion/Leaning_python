s = str(input ())
s = s.lower ()
g = 'g'
c = 'c'
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x1 = s.count (g)
x2 = s.count (c)
for x3 in s:
    x4 = x4+1
print (((x1+x2)/x4) * 100)
