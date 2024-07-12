import io
import sys
from unittest import TestCase

from stockbroker import StockBroker
from mock_driver import MockDriver

ID = 'Fake ID'
PASSWORD = 'Fake Password'


class TestMockDriver(TestCase):
    def test_mock_login(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_driver = StockBroker(MockDriver())
            stock_driver.login(ID, PASSWORD)

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        self.assertGreaterEqual(captured_output.lower().find("login"), 0)

    def test_mock_buy(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_driver = StockBroker(MockDriver())
            stock_driver.buy(222, 1000, 10)

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        self.assertGreaterEqual(captured_output.lower().find("buy"), 0)

    def test_mock_sell(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_driver = StockBroker(MockDriver())
            stock_driver.sell(222, 1000, 10)

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        self.assertGreaterEqual(captured_output.lower().find("sell"), 0)

    def test_mock_get_price(self):
        stock_driver = StockBroker(MockDriver())

        self.assertGreaterEqual(stock_driver.get_price(222), 0)