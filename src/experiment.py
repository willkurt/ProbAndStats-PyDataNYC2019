from .product import Product
from .customer import Customer
import pandas as pd

class Experiment:
    """
    This class is designed to simulate an experiment 
    """
    
    def __init__(self,product_a,product_b=None):
        self.product_a = product_a
        self.product_b = product_b


    def show_to_customers(self,n_trials):
        a_results = self._show_a_to(n_trials)
        if self.product_b:
            b_results = self._show_b_to(n_trials)
        else:
            b_results = None
        results_df = pd.DataFrame()
        if self.product_b:
            results_df['a_purchased'] = a_results['purchased']
            results_df['a_customer'] = a_results['customer']
            results_df['b_purchased'] = b_results['purchased']
            results_df['b_customer'] = b_results['customer']
        else:
            results_df['purchased'] = a_results['purchased']
            results_df['customer'] = a_results['customer']
        return results_df

    def _show_product_to(self,n,product):
        result = {
            "purchased" : [],
            "customer" : []
        }
        for i in range(n):
            rand_cust = self.generate_random_customer()
            result["purchased"].append(
                rand_cust.will_purchase(product)
                )
            result["customer"].append(str(rand_cust))
        return result
        
    
    def _show_a_to(self,n):
        return self._show_product_to(n,self.product_a)

    def _show_b_to(self,n):
        return self._show_product_to(n,self.product_b)

    def generate_random_customer(self):
        """
        Other classes may want a more complex approach to generating customers
        """
        return Customer.get_random()
