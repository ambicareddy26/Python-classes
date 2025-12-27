def prime(n):
  if n <= 1:
    return False
  for i in range(2,int(n**1/2)):
    if n%i == 0:
      return False
  return True

n = int(input())
for i in range(1,n):
  if prime(i):
    print(i,end=" ")