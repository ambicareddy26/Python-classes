s = "Ambika"
res = ""

for char in s: 
    if char.lower() not in res and char.upper() not in res:
        res += char

print(res)
