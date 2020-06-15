class User:
    min_password_length = 10  # common

    def __init__(self, name, age=None):
        self.name = name  # self.name - object (instance) attribute
        self.age = age
        self.is_logged = False

    def send_report(self):
        pass


class ReportMixin:
    def send_report(self):
        pass


class AdminUser(ReportMixin, User):
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

print(User.min_password_length)
print(AdminUser.min_password_length)
print(ManagerUser.min_password_length)

print(vars(user_1))
print(vars(User))
print(user_1.min_password_length)
# self.min_password_length -> level up -> __class__.min_password_length

user_1.min_password_length = 25  # self.min_password_length = 25
print(vars(user_1))
print(vars(User))
