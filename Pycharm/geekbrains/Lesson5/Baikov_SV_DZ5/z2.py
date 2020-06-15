# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


def rd_file(f_name):
    with open(f_name, 'r', encoding='utf-8') as my_fyle_1:
        file_content = list(map(str.strip, my_fyle_1.readlines()))
        return file_content


def sum_word(uni):
    word_2 = ' '.join(uni)
    return len(word_2.split())


f_name = 'docs/z2.txt'
user_list = rd_file(f_name)
print('количество строк {0}, количество слов {1}'.format(len(user_list), sum_word(user_list)))
