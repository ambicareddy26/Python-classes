s = "baaa"
r = "aaab"

res = {}
res1 = {}

for c in s:
    res[c] = res.get(c,0) + 1

for c in r:
    res1[c] = res1.get(c,0) + 1

def check_anagram(s,r):
    if len(s) != len(r):
        return False
    
    for ch in res:
        if ch not in res1:
            if res[ch] != res1[ch]:
                return False
            return False
    return True

print(check_anagram(r,s))