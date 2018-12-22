import unittest
from customer import Customer
import json

cust = Customer()

class testadd(unittest.TestCase):
    #def initialize(self, customers):
        #self.customers  = customers
        
    def test_add(self):
        result = cust.add_customer("90000000", "RCB", "test@rcb.com")
        self.assertIn("RCB", result)