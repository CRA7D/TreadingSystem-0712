from unittest import TestCase

from stockbroker import StockBroker


class TestStockBroker(TestCase):
    def test_input_invalid_code_when(self):
        self.sut = StockBroker()

        with self.assertRaises(Exception):
            self.sut.__invalid_check_code("123")
            self.sut.__invalid_check_code("D001234")
            self.sut.__invalid_check_code("A00123C")
            self.sut.__invalid_check_code("A0013234")

    def test_input_valid_code(self):
        self.sut = StockBroker()

        try:
            self.sut.__invalid_check_code("001234")
            self.sut.__invalid_check_code("A004562")
            self.sut.__invalid_check_code("C004562")
        except Exception:
            self.fail()
