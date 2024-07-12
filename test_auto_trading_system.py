import io
import sys
from unittest import TestCase

from stockbroker import StockBroker


class TestAutoTradingSystem(TestCase):
    def test_select_stock_brocker_kiwer선택(self):
        stock_driver = StockBroker(KiwerDriver())
        self.assertEqual(isinstance(stock_driver), KiwerDriver)

    def test_select_stock_brocker_nemo선택(self):
        stock_driver = StockBroker(KiwerDriver())
        self.assertEqual(isinstance(stock_driver), NemorDriver)

    def test_select_stock_brocker_mock선택(self):
        stock_driver = StockBroker(MockDriver())
        self.assertEqual(isinstance(stock_driver), MockDriver)

    def test_login(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(MockDriver())
            stock_driver.login()

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0,captured_output.lower().find("login"))


    def test_buy(self):
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

    def test_sell(self):
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

    def test_get_price(self):

        stock_dirver = StockBroker(MockDriver())



        self.assertGreaterEqual(0, stock_driver.get_price(222))