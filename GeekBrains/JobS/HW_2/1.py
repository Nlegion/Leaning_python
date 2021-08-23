# Проверить механизм наследования в Python.
# Для этого создать два класса.
# Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
# Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
# отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def get_name(self):
        return self.name

    @property
    def get_price(self):
        return self.price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print("товар: ", self.get_name, " цена: ", self.get_price)


item = ItemDiscountReport("Epson", 3)
item.get_parent_data()
