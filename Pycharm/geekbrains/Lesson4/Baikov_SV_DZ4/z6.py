# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle
import sys

# необходимо ввести № скрипта и его параметр

# user_call = sys.argv
user_call = 'z6.py', 2, 3, 5, 6, 71, 22, 33
pname, s_count, *start = user_call
user_list = []
if s_count == 1:
    for el in count(int(start)):
        user_call = input('Для генерации нажмите Enter, для прекращение q')
        if user_call == 'q':
            break
        else:
            print(el)
else:
    user_list.extend(s_count)
    user_list.extend(start)
    for el in cycle(user_list):
        user_call = input('Для генерации нажмите Enter, для прекращение q')
        if user_call == 'q':
            break
        print(el)
