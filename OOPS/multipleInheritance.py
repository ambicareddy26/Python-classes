class Alpha:

  def fun1(self):
    print("I am in Alpha")

class Beta:

  def fun2(self):
    print("I am in Beta")

class Gamma(Alpha,Beta):#It is a child class of both Alpha,Beta.It leads ambguity
  pass