s = [1,2,1,5,3,3,2,6,7,4,5]
#In simple we can convert the list into set by using set()
res = []
for num in s:
  if num not in res:
    res.append(num)
print(res)
