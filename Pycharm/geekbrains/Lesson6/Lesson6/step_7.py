# God object

class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.is_logged = False
        # self.inn = None


class ReportMixin:  # Mixin
    def send_report(self):
        # self.inn
        pass


class AdminUser(User, ReportMixin):
    def __init__(self, name, age=None, access_level=0):
        super().__init__(name, age)
        self.access_level = access_level


class ManagerUser(User, ReportMixin):
    def __init__(self, name, age=None, brand='0', rate=None):
        super().__init__(name, age)
        self.brand = brand
        self.rate = rate


user_1 = User('Иван')
user_2 = AdminUser('Петр', 35)
user_3 = ManagerUser('Сергей', 25, brand='Toyota', rate=5)

print(user_1, vars(user_1))
print(user_2, vars(user_2))
print(user_3, vars(user_3))

# print(user_3.name)  # ?
# print(user_3.age)  # ?
# print(user_3.inn)  # ?
