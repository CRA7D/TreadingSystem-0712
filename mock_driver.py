import random

from stockbroker import DriverInterface

ID = 'Fake ID'
PASSWORD = 'Fake Password'


class MockAPI:
    def login(self, id, password):
        print(id + ' login success')

    def buy(self, stock_code, count, price):
        print(stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))

    def sell(self, stock_code, count, price):
        print(stock_code + ' : Sell stock ( ' + str(price) + ' * ' + str(count))

    def current_price(self, stock_code) -> int:
        return random.randrange(0, 900) + 5000


class MockDriver(DriverInterface):
    def __init__(self):
        self.api = MockAPI()

    def login(self, username, password):
        if username != ID or password != PASSWORD:
            raise Exception('LoginFailException')

        self.api.login(username, password)

    def buy(self, code, price, amount):
        if code == 0 or price == 0 or amount == 0:
            raise Exception('BuyFailException')

        self.api.buy(str(code), price, amount)

    def sell(self, code, price, amount):
        if code == 0 or price == 0 or amount == 0:
            raise Exception('SellFailException')

        self.api.sell(str(code), price, amount)

    def get_price(self, code) -> int:
        if code == 0:
            raise Exception('GetPriceFailException')

        return self.api.current_price(str(code))
