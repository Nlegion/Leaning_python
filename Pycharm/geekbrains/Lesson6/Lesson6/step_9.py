# def show_user(name):
# def show_user(name, age=None):
#     return f'{name}'


class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.is_logged = False

    def __str__(self):
        return f'{self.name} ({self.age or "возраст не задан"})'

    def check_access(self):
        return bool(self.age and self.age >= 18)


user_1 = User('Иван', age=19)
print(user_1)
print(user_1.check_access())
