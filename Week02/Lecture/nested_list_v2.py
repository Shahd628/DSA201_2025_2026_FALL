def findFreqs(myList, d):
    for elem in myList:
        if not isinstance(elem, list):
            if elem not in d:
                d[elem] = 1
            else:
                d[elem] += 1
        else:
            findFreqs(elem, d)
    

if __name__ == "__main__":
    d = {}
    names = ["Adam", ["Bob", ["Alex","Bob"], "Barb", "Bert"], "Alex", ["Bea", "Alex"], "Ann"]
    findFreqs(names, d)
    maxValue = max(d.values())
    for k,v in d.items():
        if v == maxValue:
            print(k)
