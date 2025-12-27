s = [5,3,6,1,2,10]

largest = float("-inf")
second_largest = largest

for num in s:
  if num > largest:
    second_largest = largest
    largest = num
  elif num < largest and num > second_largest:
    second_largest = num

print(largest)
print(second_largest)