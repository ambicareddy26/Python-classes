class Vehicle:

  def __init__(self):
    self.noOfTyres = 2

  def fun1(self):
    print("This is in the vehicle class")

class Car(Vehicle):

  def __init__(self):
    self.name = "Swift"
    self.noOfTyres = 4
    self.price = 239090

  def drive(self):
    print("I am driving the car")

class Bike(Vehicle):
   
  def __init__(self):
    self.vehicle = "Bike"
    self.type = "Electrical"

  def ride(self):
    print("I am riding the bike")
   

c = Car()
print(c.noOfTyres)
c.drive()

b = Bike()
b.ride()