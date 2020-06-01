age = '15'
age = '18'
age = '24'
age = int(age)

if age < 18:
    print('вы слишком молоды!')
elif age < 21:
    print('есть базовый уровень доступа')
elif age < 25:
    print('есть средний уровень доступа')
else:
    print('доступ разрешен')
