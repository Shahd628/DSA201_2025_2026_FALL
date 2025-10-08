s = input("Enter a string: ")

#d = {}
d = dict()

for ch in s:
    if ch.isalpha():
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1

maxValue = max(d.values())
for k,v in d.items():
    if v == maxValue:
        print(k, v)