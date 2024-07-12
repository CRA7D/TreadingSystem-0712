import time

from stockbroker import StockBroker

TIME_INTERVAL = 1

class AutoTradingSystem:
    @property
    def stock_broker(self):
        return self.__stock_broker_driver

    def select_stocker_broker(self, stocker_broker: StockBroker) -> None:
        self.__stock_broker_driver = stocker_broker

    def login(self, id: str, passwd: str) -> bool:
        return self.__stock_broker_driver.login(id, passwd)

    def buy(self, stock_code: int, price: int, amount: int) -> bool:
        return self.__stock_broker_driver.buy(stock_code, price, amount)

    def sell(self, stock_code: int, price: int, amount: int) -> bool:
        return self.__stock_broker_driver.sell(stock_code, price, amount)

    def get_price(self, stock_code: int) -> int:
        return self.__stock_broker_driver.get_price(stock_code)

    def buy_nice_timing(self, stock_code, price):
        prev_price = self.get_price(stock_code)
        for i in range(3):
            time.sleep(TIME_INTERVAL)
            current_price = self.get_price(stock_code)

            if prev_price >= current_price:
                return 0

        self.buy(stock_code, price=current_price, amount=(price // current_price))
        return price // current_price


    def sell_nice_timing(self, stock_code, amount):
        prev_price = self.get_price(stock_code)
        for i in range(3):
            time.sleep(TIME_INTERVAL)
            current_price = self.get_price(stock_code)

            if prev_price <= current_price:
                return False

        self.sell(stock_code, price=current_price, amount=amount)
        return True
