n = int(input())
s = set()
c = 0
k = 0
while k == 0:
    if c == n:
        d = input()
        break
    else:
        a = input()
    c = c + 1
    s.add(a)
if d not in s:
    print('OK')
else:
    print('TRY ANOTHER')
