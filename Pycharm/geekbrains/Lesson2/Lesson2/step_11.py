user_data_as_list = ['Иван', 'Иванов', 25, 170, 70]

user_data = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 25,
    'height': 170,
    'weight': 70,
    # ['address', 'postman']: '',  # mutable
    ('address', 'postman'): '',  # immutable
}  # kwargs, key: value
# dns -> great dict

greeting = f'Добрый день {user_data_as_list[0]} {user_data_as_list[1]}, ' \
    f'поздравляем вас с {user_data_as_list[2]}-летием!'
print(greeting)

greeting_2 = f'Добрый день {user_data["first_name"]} {user_data["last_name"]}, ' \
    f'поздравляем вас с {user_data["age"]}-летием!'
print(greeting_2)
