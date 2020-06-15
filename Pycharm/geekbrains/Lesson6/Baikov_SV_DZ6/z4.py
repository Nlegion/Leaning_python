# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Cars:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f'Труньк!'

    def stop(self):
        return f'Тццццц!'

    def turn(self):
        return f'поворот'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        normal_speed = 60
        if self.speed > normal_speed:
            return f'Превышение скорости на {self.speed - normal_speed}'


class SportCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        normal_speed = 40
        if self.speed > normal_speed:
            return f'Превышение скорости на {self.speed - normal_speed}'


class PoliceCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


tata = SportCar(250, 'Черный', 'Tata', False)
vw = TownCar(70, 'Белый', 'VolksWagen', False)
uaz = WorkCar(70, 'Зеленый', 'УАЗ', False)
mercedes = PoliceCar(150, 'Голубой', 'Мерседес', True)

print(f'Добрый день! В эфире передача "Дорожный патруль".')
print(
    f'Сегодя сотрудники {mercedes.is_police} ГИБДД  за рулем {mercedes.color} {mercedes.name}, '
    f'на скорости {mercedes.speed} ведут свое наблюдение.')
print(
    f'Злоумышленники на {tata.color} {tata.name}, '
    f'сделали {tata.turn()} и продолжили движение со скоростью {tata.speed} км/ч')
print(f'На встречу им с {uaz.show_speed()} км/ч едет {uaz.color} {uaz.name}.')
print(f'Внезапно {uaz.color} {uaz.name} останавливается со звуком {uaz.stop()}, перегородив шоссе... Видимо поломка!')
print(
    f'{vw.go()} Это на помощь {uaz.color} {uaz.name} выдвигается {vw.color} {vw.name}, '
    f'со средней скоростью {vw.speed} и это {vw.show_speed()} км/ч')
print(f'Да... Сегодня сотрудникам ГИБДД в {mercedes.color} {mercedes.name} везет)')
print('Всем спасибо за внимание!')
