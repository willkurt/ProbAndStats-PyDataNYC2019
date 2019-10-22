import unittest
from .context import src
from src import experiment as exp
from src import customer as cust
from src import product as prod

class TestExperiment(unittest.TestCase):

    def setUp(self):
        self.test_product_a = prod.Product("a",
                                           price=2.00,
                                           quality=4.5)
        self.test_product_b = prod.Product("b",
                                           price=3.00,
                                           quality=4.9)
        self.experiment = exp.Experiment(self.test_product_a)
        self.ab_test = exp.Experiment(self.test_product_a,
                                      self.test_product_b)
        self.trials = 1000

    def test_show_to_a(self):
        results = self.experiment._show_a_to(self.trials)
        self.assertTrue(len([r for r in results["purchased"] if r]) > 0.1*self.trials)
        self.assertTrue(len([r for r in results["purchased"] if r]) < 0.9*self.trials)

    def test_show_to_customers_a(self):
        result_df = self.experiment.show_to_customers(self.trials)
        self.assertTrue('purchased' in result_df.columns)
        self.assertTrue('customer' in result_df.columns)
        self.assertTrue(result_df.shape[0] == self.trials)

    def test_show_to_customers_ab(self):
        result_df = self.ab_test.show_to_customers(self.trials)
        self.assertTrue('a_purchased' in result_df.columns)
        self.assertTrue('a_customer' in result_df.columns)
        self.assertTrue('b_purchased' in result_df.columns)
        self.assertTrue('b_customer' in result_df.columns)
        self.assertTrue(result_df.shape[0] == self.trials)

    
