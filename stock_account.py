from collections import defaultdict

from stockbroker import StockBroker


class StockAccount:
    def __init__(self, stock_broker: StockBroker):
        self.code_and_amount = defaultdict(int)
        self.cash = 100000
        self.stock_broker = StockBroker

    def get_total_asset(self):
        return self.cash + self.get_total_stock_amount()

    def get_total_stock_amount(self):
        result = 0
        for code, amount in self.code_and_amount.items():
            result += self.stock_broker.get_price(code) * amount
        return result

    def get_cash(self):
        return self.cash

    def get_amount_by(self, code):
        return self.code_and_amount[code]

    def add_stock(self, code, amount):
        self.code_and_amount[code] += amount

    def decrease_stock(self, code, amount):
        self.code_and_amount[code] -= amount


