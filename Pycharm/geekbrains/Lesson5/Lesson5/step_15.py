import pickle


def save_user(f_name, user):
    with open(f_name, 'wb') as f:
        pickle.dump(user, f)


def load_user(f_name):
    with open(f_name, 'rb') as f:
        return pickle.load(f)


# user = {
#     'name': 'Иванов Иван',
#     'age': 25,
#     'address': 'Москва, Охотный ряд'
# }
#
# save_user('user_1.pkl', user)

user = load_user('user_1.pkl')
print(type(user), user)

