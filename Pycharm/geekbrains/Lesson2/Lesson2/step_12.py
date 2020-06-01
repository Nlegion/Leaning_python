user_data = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 25,
    'height': 170,
    'weight': 70,
}

# print(user_data['weight'])
# # print(user_data['address'])
# print(user_data.get('weight', 80))
# print(user_data.get('address', 'не задан'))

address = user_data.get('address', 'Москва, Красная площадь')
print(address)
print(user_data)

address_2 = user_data.setdefault('address', 'Москва, Красная площадь')
print(address_2)
print(user_data)

address_3 = user_data.setdefault('address', 'Питер')  # do nothing
print(address_3)
print(user_data)
