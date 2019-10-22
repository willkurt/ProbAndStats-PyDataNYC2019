from .customer import Customer
import numpy as np

class StudentCustomer(Customer):
    price_mean = 0.8
    price_sd = 0.7

    def __str__(self):
        return "student"
