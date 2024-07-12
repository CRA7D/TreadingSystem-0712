from unittest import TestCase
from unittest.mock import Mock

from auto_trading_system import AutoTradingSystem
from nemo_driver import NemoDriver
from kiwer_driver import KiwerDriver


SAMPLE_ID = 'ID1234'
SAMPLE_PASSWORD = 'PW1234'
SAMPLE_STOCK_CODE = 'SC1234'
SAMPLE_STOCK_PRICE = 10000
SAMPLE_STOCK_AMOUNT = 5

INCREASED_PRICE = 11000
DECREASED_PRICE = 9000
TRADING_AMOUNT = 10


class TestAutoTradingSystem(TestCase):
    def setUp(self):
        self.sut = AutoTradingSystem()
        self.mock_stock_broker = Mock()
        self.sut.select_stocker_broker(self.mock_stock_broker)

    def test_kiwer_select_stocker_broker(self):
        kiwer = KiwerDriver()
        self.sut.select_stocker_broker(kiwer)

        self.assertEqual(kiwer, self.sut.stock_broker)

    def test_nemo_select_stocker_broker(self):
        nemo = NemoDriver()

        self.sut.select_stocker_broker(nemo)

        self.assertEqual(nemo, self.sut.stock_broker)

    def test_login(self):
        self.mock_stock_broker.login.return_value = True

        self.assertEqual(True, self.sut.login(SAMPLE_ID, SAMPLE_PASSWORD))

    def test_buy(self):
        self.mock_stock_broker.buy.return_value = True

        self.assertEqual(True, self.sut.buy(SAMPLE_STOCK_CODE, SAMPLE_STOCK_PRICE, SAMPLE_STOCK_AMOUNT))

    def test_sell(self):
        self.mock_stock_broker.sell.return_value = True

        self.assertEqual(True, self.sut.sell(SAMPLE_STOCK_CODE, SAMPLE_STOCK_PRICE, SAMPLE_STOCK_AMOUNT))

    def test_get_price(self):
        self.mock_stock_broker.get_price.return_value = SAMPLE_STOCK_PRICE

        self.assertEqual(SAMPLE_STOCK_PRICE, self.sut.get_price(SAMPLE_STOCK_CODE))

    def test_buy_nice_timing_success(self):
        self.mock_stock_broker.get_price.side_effect = [SAMPLE_STOCK_PRICE, INCREASED_PRICE]
        self.mock_stock_broker.buy.return_value = True

        self.assertEqual(TRADING_AMOUNT, self.sut.buy_nice_timing(SAMPLE_STOCK_CODE, INCREASED_PRICE * TRADING_AMOUNT))

    def test_buy_nice_timing_failure(self):
        self.mock_stock_broker.get_price.side_effect = [SAMPLE_STOCK_PRICE, DECREASED_PRICE]

        self.assertEqual(0, self.sut.buy_nice_timing(SAMPLE_STOCK_CODE, INCREASED_PRICE * TRADING_AMOUNT))

    def test_sell_nice_timing_success(self):
        self.mock_stock_broker.get_price.side_effect = [SAMPLE_STOCK_PRICE, DECREASED_PRICE]
        self.mock_stock_broker.sell.return_value = True

        self.assertEqual(True, self.sut.sell_nice_timing(SAMPLE_STOCK_CODE, TRADING_AMOUNT))

    def test_sell_nice_timing_failure(self):
        self.mock_stock_broker.get_price.side_effect = [SAMPLE_STOCK_PRICE, INCREASED_PRICE]

        self.assertEqual(False, self.sut.sell_nice_timing(SAMPLE_STOCK_CODE, TRADING_AMOUNT))
