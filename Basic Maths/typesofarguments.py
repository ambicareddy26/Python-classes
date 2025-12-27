#positional arguments
def add(a,b):
  print(a+b)

#default arguments
def multiply(a,b=2):
  print(a*b)

#variable length arguments
def numbers(*b):
  print(b)#output in tuple

#keyword variable length arguments
def details(**a):
  print(a)#output in dictionary

add(2,3)
multiply(5)
numbers(1,5,7,4)
details(name="ambika",id=530,yos=3)

