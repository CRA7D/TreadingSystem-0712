from unittest import TestCase


class TestNemoDriver(TestCase):
    def test_nemo_login(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(NemoDriver())
            stock_driver.login()

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0, captured_output.lower().find("login"))

    def test_nemo_buy(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(NemoDriver())
            stock_driver.buy(222, 1000, 10)

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0, captured_output.lower().find("buy"))

    def test_nemo_sell(self):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            stock_dirver = StockBroker(NemoDriver())
            stock_driver.sell(222, 1000, 10)

        finally:
            sys.stdout = original_stdout

        catured_output = output.getvalue()
        self.assertGreaterEqual(0, captured_output.lower().find("sell"))

    def test_nemo_get_price(self):
        stock_dirver = StockBroker(NemoDriver())
        self.assertGreaterEqual(0, stock_driver.get_price(222))