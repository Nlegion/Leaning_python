def about_person(name, age, city):
   return f'{name}, {age} год(а), проживает в городе {city}'

person_name = input('Укажите имя: ')
person_age = int(input('Укажите возраст: '))
person_city = input('Укажите город проживания: ')

print(about_person(person_name, person_age, person_city))
