def findMostFreq(numbers):
    d = {}
    for val in numbers:
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1
    
    maxFreq = max(d.values())
    result = []
    for k,v in d.items():
        if v == maxFreq:
            result.append(k)
    
    return min(result)

# main part
numbers = [1,2,1,3,2]
res = findMostFreq(numbers)
print(res)