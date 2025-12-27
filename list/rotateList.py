k = int(input())

s = [1,2,3,4,5]

k = k % len(s)

l = s[len(s)-k:] + s[:len(s)-k]

print(l)