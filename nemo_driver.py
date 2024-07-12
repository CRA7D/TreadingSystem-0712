from nemo_api import NemoAPI
from stockbroker import StockBroker, DriverInterface


class NemoDriver(DriverInterface):
    def __init__(self):
        self.api = NemoAPI()

    def login(self, username, password):
        self.api.cerification(username, password)

    def buy(self, code, price, amount):
        self.api.purchasing_stock(code, price, amount)

    def sell(self, code, price, amount):
        self.api.selling_stock(code, price, amount)

    def get_price(self, code):
        return self.api.get_market_price(code, 0)
