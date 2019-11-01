import numpy as np

class Customer:
    quality_min = 0
    quality_max = 5
    price_mean = 1
    price_sd = 0.75
    def __init__(self,
                 price_threshold,
                 quality_threshold):
        self.price_threshold = price_threshold
        self.quality_threshold = quality_threshold

    def __str__(self):
        return "customer"

    def will_purchase(self, product):
        return ( product.price <= self.price_threshold and
                 product.quality >= self.quality_threshold)
             

    @classmethod
    def get_random(cls):
        price = np.random.lognormal(cls.price_mean,cls.price_sd,1)[0]
        quality = np.random.uniform(cls.quality_min,cls.quality_max,1)[0]
        return cls(price,quality)
        
