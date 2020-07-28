def count_calls(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f'calls: {counter}')
        return func(*args, **kwargs)

    return wrapper


@count_calls
def show_greeting(name):
    print(f'Привет, {name.title()}!')


show_greeting('Иван')
show_greeting('Петр')
