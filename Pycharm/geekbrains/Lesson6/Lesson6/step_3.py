class User:
    def __init__(self):
        self.name = 'user'
        self.age = None
        self.is_logged = False


user_1 = User()  # make instance
user_2 = User()
user_3 = User()
user_4 = User()
# print(user_1)
# print(type(user_1))
# print(dir(user_1))
print(user_1.name)
print(user_1.age)
print(user_1.is_logged)

# print(vars(user_1))

user_1.name = 'Иван'  # change object (instance) state
print(user_1.name)

# 7 min -> 20:11 AIR