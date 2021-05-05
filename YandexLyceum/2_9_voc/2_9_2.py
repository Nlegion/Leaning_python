quan = int(input())
crib = {}
for i in range(quan):
    words = input().split()
    word = words[0]
    desc = words[1:len(words) + 1]
    crib[word] = desc
for i in range(int(input())):
    word = input()
    if word not in crib:
        print('Нет в словаре')
    else:
        print(*crib[word])
