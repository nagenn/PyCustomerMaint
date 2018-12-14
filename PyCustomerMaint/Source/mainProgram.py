import tornado.ioloop
import tornado.web
from customer import Customer
from addHandler import AddHandler
from delHandler import DelHandler
from getHandler import GetHandler
from exitHandler import ExitHandler
import pdb
#pdb.set_trace()
customers  = Customer()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Customers Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addcustomer", AddHandler, dict(customers = customers)),
        (r"/v1/delcustomer", DelHandler, dict(customers = customers)),
        (r"/v1/getcustomers", GetHandler, dict(customers = customers)),
        (r"/v1/exit", ExitHandler),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
