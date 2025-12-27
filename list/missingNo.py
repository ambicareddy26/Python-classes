s = [1,2,3,4,5,6,7,8,9]

# n = s[-1]

# num = n*(n+1)//2 - sum(s)
# print(num)

def missingNo(s):
  for i in range(1,len(s)+1):
    if i != s[i-1]:
      return i

print(missingNo(s))