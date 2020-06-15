# class Chair:
#     def __init__(self):
#         self.num_legs = 4
#         self.material = 'wood'
#         self.model = 'classic'

class User:
    def __init__(self):
        self.name = 'user'
        self.age = None
        self.is_logged = False


user_1 = User()  # make instance
# print(user_1)
# print(type(user_1))
# print(dir(user_1))
print(user_1.name)
print(user_1.age)
print(user_1.is_logged)

# print(vars(user_1))
