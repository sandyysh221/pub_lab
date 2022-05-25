import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Sandy", 10, 19)
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Whisky", 2, 20)

    def test_customer_has_name(self):
        self.assertEqual("Sandy", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.decrease_wallet(self.drink)
        self.assertEqual(8, self.customer.wallet)
