from abc import ABC, abstractmethod


class DriverInterface(ABC):
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


class StockBroker:
    def __init__(self, driver: DriverInterface = None):
        self.__driver = driver

    def login(self, username, password):
        self.__driver.login(username, password)

    def buy(self, code, price, amount):
        self.__driver.buy(code, price, amount)

    def sell(self, code, price, amount):
        self.__driver.sell(code, price, amount)

    def get_price(self, code):
        return self.__driver.get_price(code)
