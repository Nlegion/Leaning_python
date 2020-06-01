age = '15'
age = '18'
age = int(age)

if age < 18:
    print('вы слишком молоды!')
else:
    if age < 21:
        print('есть базовый уровень доступа')
    else:
        print('доступ разрешен')
