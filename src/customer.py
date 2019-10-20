class Customer:

    def __init__(self,
                 price_threshold,
                 quality_threshold):
        self.price_threshold = price_threshold
        self.quality_threshold = quality_threshold

    def __str__(self):
        return "todo"

    def will_purchase(self, product):
        return ( product.price <= self.price_threshold and
                 product.quality >= self.quality_threshold)
             

