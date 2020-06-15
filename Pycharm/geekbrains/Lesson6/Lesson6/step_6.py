class User:
    def __init__(self, name, age=None):
        self.name = name  # self - current object (instance)
        self.age = age
        self.is_logged = False


# class AdminUser(User):
#     pass

class AdminUser(User):
    def __init__(self, name, age=None, access_level=0):
        # User.__init__(name, age)  # very bad
        super().__init__(name, age)  # calls parent init
        self.access_level = access_level



user_1 = User('Иван')  # self = user_1
user_2 = User('Петр', 35)  # self = user_2
user_3 = User('Сергей')
# user_4 = AdminUser('Анна', 21)
user_4 = AdminUser('Анна')

print(user_1, vars(user_1))
print(user_2, vars(user_2))
print(user_3, vars(user_3))
print(user_4, vars(user_4))

print(vars(user_2).get('age'), vars(user_2)['age'])
print(user_2.age)
print(user_2.name)

print(user_4.age)
