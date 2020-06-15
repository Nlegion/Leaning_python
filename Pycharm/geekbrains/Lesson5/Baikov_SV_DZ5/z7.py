# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json


def analysis(f_name):
    income = {}
    pr = {}
    prof = 0
    prof_aver = 0
    i = 0
    with open(f_name, 'r') as file:
        for line in file:
            name, firm, earning, damage = line.split()
            income[name] = int(earning) - int(damage)
            if income.setdefault(name) >= 0:
                prof = prof + income.setdefault(name)
                i += 1  # счетчик фирм

        if i != 0:
            prof_aver = round(prof / i)  # среднее значение
        js = save_json(income)
    return prof_aver, income, js


def save_json(income):
    with open('docs/z7.json', 'w') as write_js:
        json.dump(income, write_js)
        js_str = json.dumps(income)
    return js_str


f_name = 'docs/z7.txt'
z = analysis(f_name)
print('Средняя прибыль {0}, прибыль компаний: {1}'.format(z[0], z[1]))
print('Содержимое файла json: {0}'.format(z[2]))
