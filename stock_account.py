from collections import defaultdict

from stockbroker import StockBroker


class StockAccount:
    def __init__(self, stock_broker: StockBroker):
        self.stock_list = defaultdict(int)
        self.cash = 1000000
        self.stock_broker = stock_broker

    def cnt_of_stock_class(self):
        return len(self.stock_list)

    def get_total_asset(self):
        return self.cash + self.get_total_stock_amount()

    def get_total_stock_amount(self):
        result = 0
        for code, amount in self.stock_list.items():
            result += self.stock_broker.get_price(code) * amount
        return result

    def get_cash(self):
        return self.cash

    def get_amount_by(self, code):
        return self.stock_list[code]

    def add_stock(self, code, price, amount):
        if price * amount > self.cash:
            return False
        self.stock_list[code] += amount
        self.cash -= price * amount
        return True

    def del_stock(self, code, amount):
        if self.stock_list[code] < amount:
            return False
        self.stock_list[code] -= amount
        self.cash += self.stock_broker.get_price(code) * amount
        return True

    def get_current_stock_price(self, code):
        return self.stock_broker.get_price(code) * self.stock_list[code]
