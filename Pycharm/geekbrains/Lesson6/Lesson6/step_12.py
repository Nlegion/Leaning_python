def db_auth(a, b):
    pass


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

    def login(self, name, password):
        # do we use self ???
        # do we use OOP
        db_auth(name, password)
        # ok
        db_auth(self.__name, password)


user_1 = User('Иван', age=19)
