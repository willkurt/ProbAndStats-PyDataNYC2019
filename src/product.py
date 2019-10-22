class Product:

    def __init__(self,
                 name,
                 price,
                 quality):
        self.name = name
        self.price  = price
        self.quality = quality

    def __str__(self):
        return self.name
    
