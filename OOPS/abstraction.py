from abc import ABC,abstractmethod

class Messenger:
  @abstractmethod
  def send_msg(self):
    pass

  @abstractmethod
  def rec_msg(self):
    pass

class Facebook(Messenger):

  def send_msg(self):
    print("I am sending message through facebook")

  def rec_msg(self):
    print("I am receiving message through facebook")

f = Facebook()
f.send_msg()
f.rec_msg()