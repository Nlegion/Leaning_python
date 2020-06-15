# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


def rd_file(f_name):
    with open(f_name, 'r', encoding='utf-8') as my_fyle_1:
        file_content = list(map(str.strip, my_fyle_1.readlines()))
        return file_content


def op_file(f_name):
    with open('docs/z4_ru.txt', 'w', encoding='utf-8') as my_fyle_1:
        upt_list = f_list(user_list)
        for item in range(0, len(f_list(user_list)), 3):
            upt_list[item] = f_voc(upt_list[item])
        my_fyle_1.write(' '.join(upt_list))
        return my_fyle_1


def f_list(list):
    word_2 = ' '.join(list)
    word = word_2.split()
    return word


def f_voc(z):
    voc = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    return voc.get(z)


f_name = 'docs/z4.txt'
user_list = rd_file(f_name)
op_file(f_name)
