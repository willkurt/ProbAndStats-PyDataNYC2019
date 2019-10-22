import unittest
from .context import src
from src import messy_experiment as msexp
from src import product as prod
import pandas as pd

class TestMessyExperiment(unittest.TestCase):

    def setUp(self):
        self.test_product_a = prod.Product("a",
                                           price=2.00,
                                           quality=4.5)
        self.test_product_b = prod.Product("b",
                                           price=3.00,
                                           quality=4.9)
        self.experiment = msexp.MessyExperiment(self.test_product_a)
        self.ab_test = msexp.MessyExperiment(self.test_product_a,
                                             self.test_product_b)
        self.trials = 10000

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

    def test_student_rate_a(self):
        result_df = self.experiment.show_to_customers(self.trials)
        students = sum(result_df['customer'] == 'student')
        students_rate = students/self.trials
        self.assertTrue(students_rate > 0.19)
        self.assertTrue(students_rate < 0.21)

    def test_student_rate_ab(self):
        result_df = self.ab_test.show_to_customers(self.trials)
        students_a = sum(result_df['a_customer'] == 'student')
        students_b = sum(result_df['b_customer'] == 'student')
        students_a_rate = students_a/self.trials
        students_b_rate = students_b/self.trials
        self.assertTrue(students_a_rate > 0.19)
        self.assertTrue(students_a_rate < 0.21)
        self.assertTrue(students_b_rate > 0.39)
        self.assertTrue(students_b_rate < 0.41)
        
    
