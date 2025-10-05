def checkAllLetters(s):
    d = {}
    s = s.lower()
    for ch in s:
        if ch.isalpha():
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
    if len(d.keys()) == 26:
        return "pangram"
    else:
        return "not pangram"

# main part
s = "We promptly judged antiue ivory buckles for the next prize"
res = checkAllLetters(s)
print(res)