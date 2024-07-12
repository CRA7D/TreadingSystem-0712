import io
import sys
from unittest import TestCase
from unittest.mock import Mock

from nemo_driver import NemoDriver


class TestNemoDriver(TestCase):
    def setUp(self):
        super().setUp()
        self.driver = NemoDriver()
        self.driver.api = Mock()

    def test_nemo_login(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_driver = NemoDriver()
            stock_driver.login("id", "pw")

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(catured_output.lower().find("login"), 0)

    def test_nemo_get_price(self):
        stock_driver = NemoDriver()
        self.assertGreaterEqual(stock_driver.get_price(222), 0)

    def test_nemo_login_2(self):
        self.driver.login("id", "pw")
        self.driver.api.cerification.assert_any_call("id", "pw")

    def test_nemo_buy_2(self):
        self.driver.buy(1, 1, 1)
        self.driver.api.purchasing_stock.assert_any_call(1, 1, 1)

    def test_nemo_sell_2(self):
        self.driver.sell(2, 2, 2)
        self.driver.api.selling_stock.assert_any_call(2, 2, 2)

    def test_nemo_get_price_2(self):
        self.driver.get_price(3)
        self.driver.api.get_market_price.assert_any_call(3, 0)
