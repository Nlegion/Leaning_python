# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def __init__(self, title, pen):
        super().__init__(title)
        self.pen = pen

    def draw_pen(self, title):
        return f'Запуск отрисовки. Вариант "Ручка" {self.title},{self.pen}'


class Pencil(Stationery):
    def __init__(self, title, pencil):
        super().__init__(title)
        self.pencil = pencil

    def draw_pencil(self, title):
        return f'Запуск отрисовки. Вариант "Карандаш" {self.pencil}, {self.title}'


class Handle(Stationery):
    def __init__(self, title, handle):
        super().__init__(title)
        self.handle = handle

    def draw_handle(self, title):
        return f'Вариант "маркер" {self.handle}, Запуск отрисовки, {self.title}'


primer = Stationery('Класс Мама')
pen = Pen('Класс Дочерний', 'Атрибут дочернего класса')
pencil = Pencil('Класс Дочерний', 'Атрибут дочернего класса')
handle = Handle('Класс Дочерний', 'Атрибут дочернего класса')

print(Stationery.draw(primer))
print(pen.draw_pen(pen))
print(pencil.draw_pencil(pencil))
print(handle.draw_handle(handle))
