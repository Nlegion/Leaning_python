import json


def save_user(f_name, user):
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(user, f)


def load_user(f_name):
    with open(f_name, 'r', encoding='utf-8') as f:
        return json.load(f)


# user = {
#     'name': 'Иванов Иван',
#     'age': 25,
#     'address': 'Москва, Охотный ряд'
# }
#
# save_user('user_1.json', user)

user = load_user('user_1.json')
print(type(user), user)

