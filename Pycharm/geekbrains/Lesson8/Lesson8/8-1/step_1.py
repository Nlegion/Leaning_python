"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    def __init__(self, color=None):
        self._color = color

    def running(self):
        while True:
            self.next_color()
            self.show_color()
            self._wait()

    def next_color(self):
        if self._color == 'зеленый' or not self._color:
            self._color = 'красный'
        elif self._color == 'красный':
            self._color = 'желтый'
        elif self._color == 'желтый':
            self._color = 'зеленый'

    def show_color(self):
        print(f'цвет: {self._color}')

    def _wait(self):
        if self._color == 'красный':
            sleep(7)
        elif self._color == 'желтый':
            sleep(3)
        elif self._color == 'зеленый':
            sleep(5)


class CornerTrafficLight(TrafficLight):
    def next_color(self):
        if self._color == 'зеленый' or not self._color:
            self._color = 'красный'
        elif self._color == 'красный':
            self._color = 'зеленый'


if __name__ == '__main__':
    # lighter = TrafficLight()
    # lighter = TrafficLight('желтый')
    # lighter.running()
    lighter_2 = CornerTrafficLight('красный')
    lighter_2.running()

    # lighter_2 = CornerTrafficLight('красный')
    # lighter_2.running()
    #
    # lighter_2 = CornerTrafficLight('красный')
    # lighter_2.running()
    #
    # lighter_2 = CornerTrafficLight('красный')
    # lighter_2.running()
