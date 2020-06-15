class User:
    def __init__(self, name, age=None):
        self.name = name
        self._age = age  # private
        self.is_logged = False
        self._height = None

    def __str__(self):
        return f'{self.name} ({self._age or "возраст не задан"})'

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

# user_1.age = '25'  # direct access to attribute
# use getter and setter

user_1.set_age('25')  # not direct access to attribute
# print(user_1.age)

# user_1._age = '25'

# print(vars(user_1))
# user_1.age = '25'  # bad practice
# __slots__
# print(vars(user_1))

print(user_1.check_access())

# user_1.height = 170
# print(vars(user_1))

