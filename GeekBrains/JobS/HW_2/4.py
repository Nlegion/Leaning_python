# Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
# (функция, отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print("товар: ", self.__name, " цена: ", self.__price)


item = ItemDiscountReport("Epson", 3)
item.set_price(300)
item.get_parent_data()
