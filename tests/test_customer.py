import unittest

from .context import src
from src import customer as cust
from src import product as prod


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = cust.Customer(3.00,
                                      4.2)
        self.random_customers = []
        self.n_rand = 10000
        for _ in range(self.n_rand):
            self.random_customers.append(cust.Customer.get_random())

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
               
    def test_random_quality_bounds(self):
        qs = [customer.quality_threshold for customer in self.random_customers]
        self.assertTrue(all([q > 0 for q in qs]))
        self.assertTrue(all([q < 5 for q in qs]))

    def test_random_quality_group(self):
        qs = [customer.quality_threshold for customer in self.random_customers]
        self.assertTrue(any([q > 0 and q < 1 for q in qs]))
        self.assertTrue(any([q > 1 and q < 2 for q in qs]))
        self.assertTrue(any([q > 2 and q < 3 for q in qs]))
        self.assertTrue(any([q > 3 and q < 4 for q in qs]))
        self.assertTrue(any([q > 4 and q < 5 for q in qs]))        

    def test_random_price_threshold_bounds(self):
        ps = [customer.price_threshold for customer in self.random_customers]
        self.assertTrue(all([p > 0 for p in ps]))

    def test_random_price_threshold_groups(self):
        """
        These are just general properties I want to be true
        """
        ps = [customer.price_threshold for customer in self.random_customers]
        self.assertTrue(len([p for p in ps if p < 1]) < 0.1*self.n_rand,"too low")
        self.assertTrue(len([p for p in ps if p > 50]) < 0.1*self.n_rand,"too high")
        

if __name__ == '__main__':
    unittest.main()
