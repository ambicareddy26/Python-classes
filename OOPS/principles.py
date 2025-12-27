from abc import ABC,abstractmethod

class Shapes:

  @abstractmethod
  def find_area(self):
    pass

  @abstractmethod
  def display_area(self):
    pass

class Rectangle(Shapes):
  def __init__(self):
    self.length = 10
    self.breadth = 20
    self.area = 0

  def find_area(self):
    self.area = self.length*self.breadth

  def display_area(self):
    return self.area
  
class Triangle(Shapes):
  def __init__(self):
    self.base = 5
    self.height = 20
    self.area = 0

  def find_area(self):
    self.area = self.base*self.height/2

  def display_area(self):
    return self.area
  
def areas(ref):
  ref.find_area()
  print(ref.display_area())

r = Rectangle()
t = Triangle()

areas(r)
areas(t)