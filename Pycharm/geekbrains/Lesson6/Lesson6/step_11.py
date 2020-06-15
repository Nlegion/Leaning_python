class User:
    def __init__(self, name, age=None):
        self.__name = name  # private
        self._age = age  # protected
        self.is_logged = False
        self._height = None

    def __str__(self):
        return f'{self.__name} ({self._age or "возраст не задан"})'

    def check_access(self):
        return bool(self._age and self._age >= 18)

    def set_age(self, val):
        try:
            self._age = int(val)
        except Exception as e:
            print(f'wrong age value: {val}, {e}')


user_1 = User('Иван', age=19)
print(user_1)
print(user_1.check_access())

print(user_1._age)

print(vars(user_1))
print(user_1._User__name)
# print(user_1.__name)  # name mangling
user_1.__name = 'Альберт'
print(vars(user_1))
user_1._User__name = 'Тимофей'
print(vars(user_1))
