# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def rd_file(f_name):
    with open(f_name, 'r', encoding='utf-8') as my_fyle_1:
        file_content = my_fyle_1.read()
        return file_content


def op_file(f_name):
    with open(f_name, 'w', encoding='utf-8') as my_fyle_1:
        user_list = [str(item) for item in range(100, 1001, 2)]
        my_fyle_1.write(' '.join(user_list))
        return my_fyle_1


f_name = 'docs/z5.txt'
op_file(f_name)
file_list = rd_file(f_name).split()
print('сумма:{0}'.format(sum([int(item) for item in file_list])))
