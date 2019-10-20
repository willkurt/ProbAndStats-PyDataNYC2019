class Product:

    def __init__(self,
                 name,
                 cost,
                 quality):
        self.name = name
        self.cost = cost
        self.quality = quality

    def __str__(self):
        val = "{0} ${1} {2} stars".format(self.name,
                                                self.cost,
                                                self.quality)
        return val
