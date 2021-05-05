men = int(input())
men_works = [input() for _ in range(men)]
result = 0
for example in set(men_works):
    cout = 0
    for name in men_works:
        if example == name:
            cout += 1
    if cout > 1:
        result += cout
print(result)