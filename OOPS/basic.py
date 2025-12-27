class Car:

  #instance variables
  def __init__(self):
    self.name = "Benz"
    self.colour = "Black"

  #methods 
  def accelerate(self):
    print("Car is accelerating")

c1 = Car()

print(c1.name)
print(c1.colour)

c1.accelerate()