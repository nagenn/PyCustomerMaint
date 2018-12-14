import tornado.web
#from customer import Customer
import json
import sys


class ExitHandler(tornado.web.RequestHandler):
   #def initialize(self, customers):
    #self.customers = customers
        
    sys.exit()
