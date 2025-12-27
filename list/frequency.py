s = [1,2,1,5,3,3,2,6,7,4,5]

res = {}

# for num in s:
#   if num not in res:
#     res[num] = 1
#   else:
#     res[num] += 1

for num in s:
  res[num] = res.get(num,0) + 1
print(res)