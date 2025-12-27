#Find the maximum number of consecutive one's
s = [1,1,0,1,1,1,0,0,1,1,1,1]

count = 0
max_count = 0

for num in s:
  if num == 1:
    count += 1
  else:
    if count > max_count:
      max_count = count
    count = 0
    
if count > max_count:
  max_count = count

print(max_count)