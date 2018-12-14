import tornado.web
from customer import Customer
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, customers):
        print("Init")
        self.customers  = customers
        
    def get(self):
        print("Inside addhandler")
        name = self.get_argument('Name')
        mobile = self.get_argument('Mobile')
        email = self.get_argument('Email')
        result = self.customers.add_customer(name, mobile, email)
        self.write(result)
