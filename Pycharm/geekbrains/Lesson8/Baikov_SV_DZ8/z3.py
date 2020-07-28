# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

import re


class ReadDataError(Exception):
    def __init__(self, msg, data, data2):
        self.msg = msg
        self.data = data
        self.data2 = data2


class AvgCalcError(Exception):
    pass


def read_data():
    result = []
    while True:
        try:
            line = input('вводите через пробел числа (или нажмите ВВОД): ')
            if 'stop' in line:
                raise SystemExit
            elif not line:
                return result

            result.extend(map(float, line.split()))
            result2 = [float(item) for item in (re.sub(r'[^0-9]', ' ', line)).split()]

        except Exception as e:
            raise ReadDataError(f'data read failed: {e}', result, result2)
        return result


def user_code():
    data = read_data()
    try:
        avg = sum(data) / len(data)
        print(f'среднее значение на {len(data)} числах: {avg:.2f}')
    except Exception as e:
        raise AvgCalcError(f'average val calculation failed: {e}')


def calc(data2):
    avg = sum(data2) / len(data2)
    print(f'среднее значение на {len(data2)} числах: {avg:.2f}')


if __name__ == '__main__':
    while True:
        try:
            user_code()
        except ReadDataError as e:
            print(f'ошибка ввода данных: {e}')
            print(f'\tуспели ввести до ошибки: {e.data}')
            print(f'\tввели числа: {e.data2}')
            calc(e.data2)
        except AvgCalcError as e:
            print(f'не смогли вычислить среднее: {e}')
        except Exception as e:
            print(f'непредвиденная ошибка: {e}')
