# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


def rd_file(f_name):
    with open(f_name, 'r', encoding='utf-8') as my_fyle_1:
        file_content = list(map(str.strip, my_fyle_1.readlines()))
        return file_content


def f_mean(mean):
    sum = 0
    z = 0
    for item in range(1, len(mean), 2):
        sum += int(mean[item])
        z += 1
    return sum / z


def f_list(list):
    word_2 = ' '.join(list)
    word = word_2.split()
    return word


def min_zp(zp):
    user_min_zp = []
    for item in range(1, len(zp), 2):
        if int(zp[item]) <= 20000:
            user_min_zp.append(zp[item - 1])
    return user_min_zp


f_name = 'docs/z3.txt'
user_list = rd_file(f_name)
mod_list = f_list(user_list)

print('Сотрудники с окладом менее 20 тыс. {0}, средняя ЗП:{1}'.format(min_zp(mod_list), f_mean(mod_list)))
