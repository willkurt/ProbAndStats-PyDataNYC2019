class Customer:

    def __init__(self,
                 price_threshold,
                 quality_threshold):
        self.price_threshold = price_threshold
        self.quality_threshold = quality_threshold

    def __str__(self):
        return "todo"

    def will_purchase(product):
        return ( product.price <= self.price_threshold and
                 produce.quality >= self.quality_threshold)
             

