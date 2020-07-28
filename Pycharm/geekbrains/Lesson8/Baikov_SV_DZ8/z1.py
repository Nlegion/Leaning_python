# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, user_data):
        self.u_data = str(user_data)

    @classmethod
    def ext(cls, u_data):
        day, month, year = [int(item) for item in u_data.split('-')]
        return f'{day}:{month}:{year}'

    @staticmethod
    def valid(u_data):
        day, month, year = [int(item) for item in u_data.split('-')]
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Дата правильная'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'{Data.valid(self.u_data)}: {Data.ext(self.u_data)}'


today = Data('23 - 5 - 2020')
print(today)
