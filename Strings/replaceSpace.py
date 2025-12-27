s = "Iam studying in AU"

res =""

for char in s:
    if char == " ":
        res += '%'
    else:
        res += char

print(res)