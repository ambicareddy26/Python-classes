s = "AmbikazZ"

#lowerCase to upperCase
def lower_case(s):
    res = ""
    for ch in s:
        if ord(ch) > 91:
            res += chr(ord(ch) - 32)
        else:
            res += ch
    print(res)

def upper_case(s):
    res = ""
    for ch in s:
        if ord(ch) < 97:
            res += chr(ord(ch) + 32)
        else:
            res += ch

    print(res)

lower_case(s)
upper_case(s)