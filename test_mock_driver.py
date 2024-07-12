import io
import sys
from unittest import TestCase


class TestMockDriver(TestCase):
    def test_mock_login(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(MockDriver())
            stock_driver.login()

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0, captured_output.lower().find("login"))

    def test_mock_buy(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(MockDriver())
            stock_driver.buy(222, 1000, 10)

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0, captured_output.lower().find("buy"))

    def test_mock_sell(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(MockDriver())
            stock_driver.sell(222, 1000, 10)

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0, captured_output.lower().find("sell"))

    def test_mock_get_price(self):
        stock_dirver = StockBroker(MockDriver())

        self.assertGreaterEqual(0, stock_driver.get_price(222))