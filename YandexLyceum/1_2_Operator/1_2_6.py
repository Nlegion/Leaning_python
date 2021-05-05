y = input()
x = input()

if '@' in y:
    print("Некорректный логин")
else:
    if '@' not in x:
        print("Некорректный адрес")
    else:
        print('OK')