from abc import ABC, abstractmethod


class StockBroker(ABC):
    def __init__(self, driver=None):
        self.select_stock_brocker(driver)

    def select_stock_brocker(self, driver):
        self.__driver = driver

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def buy(self, code, price, amount):
        pass

    @abstractmethod
    def sell(self, code, price, amount):
        pass

    @abstractmethod
    def get_price(self, code):
        pass
