# while True:
#     age = input('введите возраст ')
#     if age.isdigit():
#         age = int(age)
#         break
#     # continue  # bad idea

# age = input('введите возраст ')
age = 'zsdfsdfdf'
while not age.isdigit():  # [0-9]+ '515792131089151'
    # age = input('введите возраст ')
    age = '25'

age = int(age)
print(f'ваш возраст: {age:03d} лет')
