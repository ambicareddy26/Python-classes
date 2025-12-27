class Messenger:

  def send_msg(self):
    pass

  def rec_msg(self):
    pass

class Facebook(Messenger):

  def send_msg(self):
    print("I am sending message through facebook")

  def rec_msg(self):
    print("I am receiving message through facebook")

class Whatsapp(Messenger):

  def send_msg(self):
    print("I am sending message through whatsapp")

  def rec_msg(self):
    print("I am receiving message through whatsapp")

  def live_location(self):
    print("Sharing live location")

class Instagram(Messenger):

  def send_msg(self):
    print("I am sending message through Instagram")

  def rec_msg(self):
    print("I am receiving message through Instagram")
  
def display(ref):
  ref.send_msg()
  ref.rec_msg()
  if ref == w:
    ref.live_location()

f = Facebook()
w = Whatsapp()
i = Instagram()

display(f)
display(w)
display(i)

