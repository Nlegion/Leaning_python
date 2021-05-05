s1 = input()
s2 = input()
bull = 0
cow = 0
for i in zip(s1, s2):
    if i[0] == i[1]:
        bull += 1
    elif i[0] in s2:
        cow += 1
print(bull, cow)
