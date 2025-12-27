n = [1,2,5,1,4,6,2,10,5]

res = {}

for num in n:
  # if num not in res:
  #   res[num] = 1
  # else:
  #   res[num] += 1
  res[num] = res.get(num,0) + 1

print(res)