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
        self.experiment = exp.Experiment(self.test_product_a)
        self.trials = 1000

    def test_show_to_a(self):
        results = self.experiment._show_a_to(self.trials)
        self.assertTrue(len([r for r in results["purchased"] if r]) > 0.1*self.trials)
        self.assertTrue(len([r for r in results["purchased"] if r]) < 0.9*self.trials)

    
