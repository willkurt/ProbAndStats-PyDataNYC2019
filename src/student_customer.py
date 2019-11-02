from .customer import Customer
import numpy as np

class StudentCustomer(Customer):
    price_mean = 0.97
    price_sd = 0.2

    def __str__(self):
        return "student"



