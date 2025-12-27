s = [2,5,1,0,8,4,0,0,3]

l = [num for num in s if num != 0]

noOfZeroes = len(s) - len(l)

l = l + [0]*noOfZeroes

print(l)
