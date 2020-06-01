# first_name, last_name, age = 'Иван', 'Иванов', 25
# print(first_name, last_name, age)

# user_data = 'Иван Иванов 25'
# user_data = 'Иван-Иванов-Борисов-25'
# print(user_data.split(':'))
# print(user_data.split('-', maxsplit=1))
# print(user_data.split('-'))

# user_data = 'Иван Иванов 25'
# first_name, last_name, age = user_data.split()
# print(first_name, last_name, age)

user_data = 'Иван Иванов 25 170 70'
first_name, last_name, age, *others = user_data.split()
print(first_name, last_name, age)
print(others)

