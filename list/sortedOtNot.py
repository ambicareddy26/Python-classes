
def isSorted(s):
  for i in range(1,len(s)):
    if s[i] < s[i-1]:
      return False
  return True

s = [1,1,1,1,2,5,5,5,5,6]

print("Is the list sortes?:",isSorted(s))
