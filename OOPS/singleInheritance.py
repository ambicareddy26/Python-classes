class Vehicle:
  
  def fun1(self):
    print("This is in the vehicle class")

class Car(Vehicle):

  def fun(self):
    print("This vehicle is a car")

c = Car()
c.fun1()
c.fun()