class Customer:
  def __init__(self,name,pnumber,address):
    self.name = name
    self.pnumber = pnumber
    self.address = address

  def order(self):
    print("Customer is ordering.....")

  def payment(self):
    print("Payment is successful")

class GoldCustomer(Customer):
  def __init__(self, name, pnumber, address,goldId):
    super().__init__(name, pnumber, address)
    self.goldId = goldId
   
  def freeDelivery(self):
    print("No delivery cost")

g = GoldCustomer("Ambika",34763483295,"Kadapa",1)
print(g.name)
print(g.address)
g.payment()
g.freeDelivery()

    