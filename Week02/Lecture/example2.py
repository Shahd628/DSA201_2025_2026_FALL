s = input("Enter a string: ")

mySet = set() # empty set initially

for ch in s:
    if ch.isalpha():
        mySet.add(ch)

print(len(mySet))

