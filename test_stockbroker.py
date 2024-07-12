from unittest import TestCase
from unittest.mock import Mock

from stockbroker import StockBroker


class TestStockBroker(TestCase):
    def setUp(self):
        mock = Mock()
        self.sut = StockBroker(mock)

    def test_input_invalid_code_when(self):
        with self.assertRaises(Exception):
            self.sut.get_price("123")
            self.sut.get_price("D001234")
            self.sut.get_price("A00123C")
            self.sut.get_price("A0013234")

    def test_input_valid_code(self):
        try:
            self.sut.get_price("001234")
            self.sut.get_price("A004562")
            self.sut.get_price("C004562")
        except Exception:
            self.fail()
