import io
import sys
from unittest import TestCase
from unittest.mock import Mock

from kiwer_driver import KiwerDriver
from stockbroker import StockBroker


TEST_ID = "hello"
TEST_PASSWORD = "w!o@r#l$d%"
TEST_CODE = "WBTN"
TEST_PRICE = 10000
TEST_AMOUNT = 300


class TestKiwerDriver(TestCase):
    def setUp(self):
        external_api = Mock()
        external_api.login.side_effect = lambda x, y: print("login")
        external_api.buy.side_effect = lambda x, y, z: print("buy")
        external_api.sell.side_effect = lambda x, y, z: print("sell")
        external_api.current_price.return_value = 100
        self.sut = KiwerDriver()
        self.sut.set_api(external_api)

    def test_kiwer_login(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            self.sut.login(TEST_ID, TEST_PASSWORD)

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        self.assertGreaterEqual(captured_output.lower().find("login"), 0)

    def test_kiwer_buy(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            self.sut.buy(TEST_CODE, TEST_PRICE, TEST_AMOUNT)

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        self.assertGreaterEqual(captured_output.lower().find("buy"), 0)

    def test_kiwer_sell(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            self.sut.sell(TEST_CODE, TEST_PRICE, TEST_AMOUNT)

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        self.assertGreaterEqual(captured_output.lower().find("sell"), 0)

    def test_kiwer_get_price(self):
        self.assertEqual(100, self.sut.get_price(TEST_CODE))

    def test_kiwer_login_should_raise_type_error_when_not_valid_arg(self):
        with self.assertRaises(TypeError) as te:
            self.sut.login(123, 456)