
import json
#from Carbon.Aliases import false

class Customer:
    
    def __init__(self):
        self.customers= []
        
    def add_customer(self, customer_name, customer_mobile, customer_email):
        print("Inside customer")
        new_customer = {}
        new_customer["Name"] = customer_name
        new_customer["Mobile"] = customer_mobile
        new_customer["Email"] = customer_email
        self.customers.append(new_customer)
        print("Customer: {0}".format(new_customer))
        return json.dumps(new_customer)
        
    def del_customer(self, customer_email):
        found = False
        for idx, customer in enumerate(self.customers):
            if customer["Email"] == customer_email:
                index = idx
                found = True
                del self.customers[idx]
        print("Customers: {0}".format(json.dumps(self.customers)))
        return found

    def get_all_customers(self):
        return self.customers

    def json_list(self):
        return json.dumps(self.customers)

            