from .product import Product
from .customer import Customer
from .student_customer import StudentCustomer
from .experiment import Experiment

import numpy as np

class MessyExperiment(Experiment):
    """
    This is a messier version of the experiment in which
    there are student customers as well and student customers
    tend to have lower prices thresholds, meaning they are more
    sensitive to expensive products.

    What's worse is that variant b (if there is one) will 
    systematically get more student customers than variant a.
    This means we must model this is we are going to make
    any decisions about which variant is better.
    """
    def _show_with_students(self,n,rate,product):
        result = {
            "purchased" : [],
            "customer" : []
        }
        for i in range(n):
            if np.random.uniform(0,1,1) < rate:
                rand_cust = StudentCustomer.get_random()
            else:
                rand_cust = Customer.get_random()
            result["purchased"].append(
                rand_cust.will_purchase(product)
                )
            result["customer"].append(str(rand_cust))
        return result
        
    
    def _show_a_to(self,n):
        return self._show_with_students(n,0.1,self.product_a)

    def _show_b_to(self,n):
        return self._show_with_students(n,0.4,self.product_b)

    
