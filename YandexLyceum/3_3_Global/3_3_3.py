class Receipt:

    def __init__(self):
        self.number = 1
        self.amount = 0
        self.cost = 0
        self.lines = []

    def add_item(self, item, cost):
        self.amount += 1
        self.lines.append("%s - %s" % (item, str(cost)))
        self.cost += cost

    def new(self):
        self.number += 1
        self.amount = 0
        self.cost = 0
        self.lines = []

    def print(self):
        if self.amount != 0:
            print("Чек %s. Всего предметов: %s" % (self.number, self.amount))
            for line in self.lines:
                print(line)
            print("Итого: %s" % self.cost)
            print("-----")
            self.new()


r = Receipt()


def add_item(item, cost, receipt=r):
    receipt.add_item(item, cost)


def print_receipt(receipt=r):
    r.print()
