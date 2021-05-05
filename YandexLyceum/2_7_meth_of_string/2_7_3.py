a = input().lower()
a = a.replace(" ", "")
text = list(a)
text.sort()
index = 0
a = 0
b = 0
c = []
n = []
for i in range(0, len(text)):
    if text[i] != text[i - 1] or i == len(text) - 1:
        c.append(text[i - 1])
        n.append(index)
        index = 0
    else:
        index += 1
maxs = 0
num = 0
for j in range(len(n)):
    if n[j] > maxs:
        maxs = n[j]
        num = j
print(c[num])
