from unittest import TestCase
from unittest.mock import Mock

from stock_account import StockAccount
from stockbroker import StockBroker


class TestStockAccount(TestCase):

    def setUp(self):
        stock_broker = Mock()
        stock_broker.get_price.return_value = 100
        self.sut = StockAccount(stock_broker)
    def test_buy_stock(self):
        self.sut.add_stock("001234", 2000, 3)
        self.sut.add_stock("003456", 3000, 2)

        self.assertEqual(2, self.sut.cnt_of_stock_class())

    def test_buy_stock_same_product(self):
        self.sut.add_stock("003344", 2000, 3)
        self.sut.add_stock("003344", 2000, 3)

        self.assertEqual(1, self.sut.cnt_of_stock_class())
        self.assertEqual(6, self.sut.stock_list["003344"])

    def test_sell_stock_normal(self):
        self.sut.add_stock("003344", 2000, 3)

        self.assertTrue(self.sut.del_stock("003344", 2))

    def test_sell_stock_more_than_count(self):
        self.sut.add_stock("003344", 2000, 3)
        self.assertFalse(self.sut.del_stock("003344", 4))

    def test_get_current_total_price_when_no_stock(self):
        self.assertEqual(1000000, self.sut.get_cash())

    def test_get_current_total_price_when_one_stock(self):
        self.sut.add_stock("003344", 2000, 3)

        self.assertEqual(300, self.sut.get_current_stock_price("003344"))


