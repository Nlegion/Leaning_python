class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.is_logged = False


user_1 = User('Иван')
user_2 = User('Петр', 35)
user_3 = User('Сергей')
user_4 = User('Анна', 21)

print(user_1, vars(user_1))
print(user_2, vars(user_2))
print(user_3, vars(user_3))
print(user_4, vars(user_4))

print(vars(user_2).get('age'), vars(user_2)['age'])
print(user_2.age)
print(user_2.name)

