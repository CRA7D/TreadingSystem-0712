from unittest import TestCase
from unittest.mock import Mock

from stockbroker import StockBroker


class TestStockAccount(TestCase):
    def test_buy_stock(self):
        sut = StockAccount()
        sut.add_stock("001234", 2000, 3)
        sut.add_stock("003456", 3000, 2)

        self.assertEqual(2, sut.stock_list)

    def test_buy_stock_same_product(self):
        sut = StockAccount()
        sut.add_stock("003344", 2000, 3)
        sut.add_stock("003344", 2000, 3)

        self.assertEqual(1, sut.stock_list)
        self.assertEqual(6, sut.stock_list["003344"]["cnt"])

    def test_sell_stock_normal(self):
        sut = StockAccount()
        sut.add_stock("003344", 2000, 3)

        self.assertTrue(sut.del_stock("003344", 2))

    def test_sell_stock_more_than_count(self):
        sut = StockAccount()
        sut.add_stock("003344", 2000, 3)
        self.assertFalse(sut.del_stock("003344", 4))

    def test_get_current_total_price_when_no_stock(self):
        sut = StockAccount()
        self.assertEqual(1000000, sut.get_total_price())

    def test_get_current_total_price_when_one_stock(self):
        sut = StockAccount()
        stb = Mock(spec=StockBroker())
        stb.get_price.return_value = 3000

        sut.add_stock("003344", 2000, 3)

        self.assertEqual(9000, sut.get_current_stock_price("003344"))


