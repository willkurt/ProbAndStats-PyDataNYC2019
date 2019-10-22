import unittest

from .context import src
from src import customer as cust
from src import student_customer as stcust

class TestStudentCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = cust.Customer(3.00,
                                      4.2)
        self.stcustomer = stcust.StudentCustomer(3.00,
                                                 4.2)
        self.n_rand = 10000
        self.random_customers = []
        self.random_student_customers = []
        for _ in range(self.n_rand):
            self.random_customers.append(cust.Customer.get_random())
            self.random_student_customers.append(
                stcust.StudentCustomer.get_random()
                )

    def test_to_string_diff(self):
        self.assertFalse(str(self.customer) == str(self.stcustomer))

    
    def test_diff_in_mean(self):
        mean_cust = sum([cust.price_threshold for cust in self.random_customers])/self.n_rand
        mean_st = sum([st.price_threshold for st in self.random_student_customers])/self.n_rand
        self.assertTrue((mean_cust > mean_st))

    def test_diff_in_max(self):
        max_cust = max([cust.price_threshold for cust in self.random_customers])
        max_st = max([st.price_threshold for st in self.random_student_customers])
        self.assertTrue((max_cust - max_st) > 10)
