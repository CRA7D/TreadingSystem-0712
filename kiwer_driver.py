from kiwer_api import KiwerAPI
from stockbroker import DriverInterface


class KiwerDriver(DriverInterface):
    def __init__(self):
        # 외부 API와 전용 driver는 필연적으로 연결된 객체 들이니 굳이 주입 받지 않는다.
        self.__api = KiwerAPI()

    # 그래도 혹시 변경될 수 있으니 setter는 구현해두었다.
    def set_api(self, external_api: KiwerAPI):
        self.__api = external_api

    def login(self, username: str, password: str):
        self.__validation_arg_str(username, password)
        self.__api.login(username, password)

    def buy(self, code: str, price: int, amount: int):
        self.__validation_arg_str(code)
        self.__validation_arg_int(price, amount)
        self.__api.buy(code, price, amount)

    def get_price(self, code: str):
        self.__validation_arg_str(code)
        return self.__api.current_price(code)

    def sell(self, code: str, price: int, amount: int):
        self.__validation_arg_str(code)
        self.__validation_arg_int(price, amount)
        self.__api.sell(code, price, amount)

    def __validation_arg_str(self, *args):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("{arg}는 str 형식으로 입력해야 합니다.")

    def __validation_arg_int(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("{arg}는 int 형식으로 입력해야 합니다.")