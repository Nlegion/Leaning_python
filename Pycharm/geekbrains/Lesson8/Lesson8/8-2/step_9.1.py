class ReadDataError(Exception):
    pass


class AvgCalcError(Exception):
    pass


class MyList:
    pass


def read_data():
    result = []
    while True:
        try:
            line = input('вводите через пробел числа (или нажмите ВВОД): ')
            if not line:
                return result
            result.extend(map(float, line.split()))
        except Exception as e:
            raise ReadDataError(f'data read failed: {e}')


def user_code():
    data = read_data()
    try:
        avg = sum(data) / len(data)
        print(f'среднее значение на {len(data)} числах: {avg:.2f}')
    except Exception as e:
        raise AvgCalcError(f'average val calculation failed: {e}')
    # except AvgCalcError as e:  # bad idea
    #     print('что-то случилось')


if __name__ == '__main__':
    try:
        user_code()
    except ReadDataError as e:
        print(f'ошибка ввода данных: {e}')
    except AvgCalcError as e:
        print(f'не смогли вычислить среднее: {e}')
    except Exception as e:
        print(f'непредвиденная ошибка: {e}')
