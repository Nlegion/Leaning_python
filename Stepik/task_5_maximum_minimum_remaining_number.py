a = int(input ())
b = int(input ())
c = int(input ())
x = a
y = a
z = a + b + c
if x <= b: x = b
if x <= c: x = c
print (x)
if y >= b: y = b
if y >= c: y = c
print (y)
print (z-(x+y))
