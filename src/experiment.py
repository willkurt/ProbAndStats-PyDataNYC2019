from product import Product
from customer import Customer

class Experiment:
    """
    This class is designed to simulate an experiment 
    """
    
    def __init__(self,product_a,product_b=None):
        self.product_a = product_a
        self.product_b = product_b


    def show_to_customers(self,n_trials):
        a_results = self._show_a_to(n)
        if self.product_b:
            b_results = self._show_b_to(n)
        else:
            b_results = None
        pass



    def _show_a_to(self,n):
        """
        
        """
        pass

    def generate_random_customer(self):
        return Customer.get_random()
