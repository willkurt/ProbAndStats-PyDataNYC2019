import unittest

from .context import src
from src import customer as cust
from src import product as prod


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = cust.Customer(3.00,
                                      4.2)

    def test_price_too_high(self):
        too_expensive = prod.Product("a",
                                     3.01,
                                     4.3)
        self.assertFalse(
            self.customer.will_purchase(too_expensive)
            )

    def test_quality_too_low(self):
        poor_quality = prod.Product("a",
                                     1.0,
                                     3.0)
        self.assertFalse(
            self.customer.will_purchase(poor_quality)
            )
                            

    def test_just_right(self):
        goldilocks = prod.Product("a",
                                  3.0,
                                  4.2)
        self.assertTrue(
            self.customer.will_purchase(goldilocks)
            )
                            

    def test_great_choice(self):
        great_product = prod.Product("a",
                                     0.2,
                                     5)
        self.assertTrue(
            self.customer.will_purchase(great_product)
            )
               
                                     

if __name__ == '__main__':
    unittest.main()
