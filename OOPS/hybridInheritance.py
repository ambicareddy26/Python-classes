class Vehicle:
  
  def fun1(self):
    print("This is in the vehicle class")

class Car(Vehicle):

  def fun(self):
    print("This vehicle is a car")

class Electric(Car):

  def electric(self):
    print("This is an electrical car")

class Fuel(Car):

  def fuel(self):
    print("This car is of fuel type");

e = Electric()
e.fun1()
e.fun()
e.electric()

f = Fuel()
f.fuel()