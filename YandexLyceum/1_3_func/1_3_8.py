print(*sorted((int(input()) for _ in range(3)), reverse=True), sep="\n")
a = int(input())
b = int(input())
c = int(input())

if a > b > c:
    print(a)
    print(b)
    print(c)

elif a > c > b:
    print(a)
    print(c)
    print(b)

elif b > a > c:
    print(b)
    print(a)
    print(c)

elif b > c > a:
    print(b)
    print(c)
    print(a)

elif c > a > b:
    print(c)
    print(a)
    print(b)

elif c > b > a:
    print(c)
    print(b)
    print(a)

elif a == b == c:
    print(b)
    print(c)
    print(a)