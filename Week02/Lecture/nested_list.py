def countUniqueNames(myList):
    counter = 0
    for elem in myList:
        if not isinstance(elem, list):
            counter += 1
        else:
            counter += countUniqueNames(elem)
    return counter


names = ["Adam", ["Bob", ["Chet","Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
res = countUniqueNames(names)
print(res)