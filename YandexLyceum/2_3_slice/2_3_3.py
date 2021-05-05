s = input()
maxx = 0
temp = 0
for i in s:
    if i == 'о':
        temp += 1
        if temp > maxx:
            maxx = temp
    else:
        temp = 0
print(maxx)