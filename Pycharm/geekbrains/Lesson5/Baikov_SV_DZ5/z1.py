# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

def rd_file(f_name):
    with open(f_name, 'r', encoding='utf-8') as my_fyle_1:
        file_content = my_fyle_1.read()
        return file_content


def op_file(f_name, body):
    with open(f_name, 'w', encoding='utf-8') as my_fyle_1:
        idx = 0
        while idx < len(body):
            my_fyle_1.write(body[idx] + '\n')
            idx += 1
        return my_fyle_1


f_name = 'docs/z1.txt'
user_call = input('Введите текст. Для прекращения оставьте строку пустой')
user_list = []
while True:
    if user_call == '':
        op_file(f_name, user_list)
        print(rd_file(f_name))
        break
    else:
        user_list.append(user_call)
    user_call = input('Введите текст. Для прекращения оставьте строку пустой')
