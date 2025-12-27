class Instagram:

  def __init__(self):
    self.id = "Brama123"
    self.__password = 874543

  def setpassword(self,p):
    self.__password = p

  def getpassword(self):
    return self.__password
  
I = Instagram()

I.setpassword(327648391)
print(I.getpassword())