class OrderRecord:
    quantity = 0
    item_price = 0

    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price


class Order:
    def __init__(self, a_record):
        self.data = a_record

    def quantity(self):
        return self.data.quantity

    def item_price(self):
        return self.data.item_price

    def price(self):
        """"price is base prince - quantity discount + shipping"""
        return self.quantity() * self.item_price() - max(0, self.quantity() - 500) * self.item_price() * 0.05 + min(
            self.quantity() * self.item_price() * 0.1, 100)


if __name__ == '__main__':
    record = OrderRecord(100, 10)
    print(Order(a_record=record).price())
