from abc import ABC, abstractmethod
import re


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

    def __validate_code(self, code):
        pattern = r"^[A-C|K]?\d{6}$"
        if not re.match(pattern, code):
            raise Exception("Invalid stock code")

    def login(self, username, password):
        self.__driver.login(username, password)

    def buy(self, code, price, amount):
        self.__validate_code(code)
        self.__driver.buy(code, price, amount)

    def sell(self, code, price, amount):
        self.__validate_code(code)
        self.__driver.sell(code, price, amount)

    def get_price(self, code):
        self.__validate_code(code)
        return self.__driver.get_price(code)
