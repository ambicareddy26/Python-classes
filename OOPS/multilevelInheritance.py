class Alpha:
  def fun1(self):
    print("I am in Alpha")
  
class Beta(Alpha):
  def fun2(self):
    print("I am in Beta")

class Gamma(Beta):
  def fun3(self):
    print("I am in Gamma")

b = Beta()
b.fun1()
b.fun2()

g = Gamma()
g.fun3()
g.fun2()

