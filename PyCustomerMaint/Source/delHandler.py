import tornado.web
from customer import Customer
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, customers):
        self.customers = customers
        
    def get(self):
        email = self.get_argument('Email')
        result = self.customers.del_customer(email)
        if result:
            self.write("Deleted customer with email: {0} successfully".format(email))
            self.set_status(200)
        else:
            self.write("Customer email '{0}' not found".format(email))
            self.set_status(404)
