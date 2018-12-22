import tornado.web
import os
import json



class ExitHandler(tornado.web.RequestHandler):
    def initialize(self):
       print("Thank you for using the Customer Maintenance program")
        
    def get(self):
        os._exit(0)

