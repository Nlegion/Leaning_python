#u1 = int(input('введите число'))
u1 = 3
num = 0 #счетчик
z1 = 0
z2 = 0
while u1 > num:
    q = u1 * 10 ** num
    z1 = z1 + q
    z2 = z2 + z1
    num = num + 1
print (z2)
