# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for item in self.__color:
            print(item)
            if item == 'Red':
                sleep(7)
            elif item == 'Yellow':
                sleep(2)
            else:
                sleep(10)


print('Вариант 1')
color = TrafficLight(['Red', 'Yellow', 'Green'])
TrafficLight.running(color)


class TrafficLight2:
    colors = ['Красный', 7, 'Желтый', 2, 'Зеленый', 3]
    item = 0

    def __init__(self):
        self.__color = self.colors[0]  # private
        self.time = self.colors[1]  # private

    def check_color(self):
        if self.__color == 'Красный':
            item = 2
        elif self.__color == 'Желтый':
            item = 4
        else:
            item = 0
        return item

    def change_color(self):
        item = self.check_color()
        self.__color = self.colors[item]
        self.time = self.colors[item + 1]

    def running(self):
        while True:
            print(self.__color)
            sleep(self.time)
            self.change_color()


print('Вариант 2')
color2 = TrafficLight2()
TrafficLight2.running(color2)
