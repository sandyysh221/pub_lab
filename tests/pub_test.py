import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

# from folder.file import Class

# 3 A's of testing: Arrange, Act, Assert
# Arrange: set up test enviroment
# Act: perform action we are testing
# Assert: perform test


class TestPub(unittest.TestCase):
    # this class inherits from unittest.TestCase
    def setUp(self):
        # runs before each test creating data used for the tests
        self.customer0 = Customer("Sandy", 10, 19)
        self.customer1 = Customer("Kenny", 0, 40)
        self.customer2 = Customer("Bilbo", 10, 5)
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Whisky", 2, 20)

    def test_pub_has_name(self):
        # test_ identifies this as a test to be run, to the IDE
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        # (expected, actual)
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_can_sell_drink_to_customer(self):
        self.assertEqual(
            True, self.pub.check_enough_cash(self.customer0, self.drink.price)
        )
        self.assertEqual(True, self.pub.confirmed_age(self.customer0))

    def test_drink_sold(self):
        self.pub.increase_till(self.drink.price)
        self.assertEqual(102, self.pub.till)
        self.customer0.decrease_wallet(self.drink.price)
        self.assertEqual(8, self.customer0.wallet)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink, self.customer0)
        self.assertEqual(102, self.pub.till)
        self.assertEqual(8, self.customer0.wallet)

    # def test_sell_drink__no_money(self):
    #     self.pub.sell_drink(self.drink.price, self.customer1)
    #     self.assertEqual(100, self.pub.till)
    # #     self.assertEqual(0, self.customer1.wallet)

    def test_sell_drink__underaged(self):
        self.pub.sell_drink(self.drink.price, self.customer2)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(10, self.customer2.wallet)
