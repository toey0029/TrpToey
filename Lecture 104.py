class Customer:
    name = ""
    lastName = ""
    age = 0

    def addClart(self):
        print("Added to Card",self.name,self.lastName,"'s card")

customer1 = Customer()
customer1.name = "Kittikorn"
customer1.lastName = "P"
customer1.addClart()