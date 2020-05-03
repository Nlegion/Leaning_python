a = int (input())
b = int (input())
z = 0
y = 0
for i in range (a,b+1,1):
    if (i%3) == 0:
        y = y + 1
        z = z + i
print (z/y)
