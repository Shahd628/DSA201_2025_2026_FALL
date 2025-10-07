"""
10
9
8
7
6
5
4
3
2
1
"""

def countdown_without_recursion(num):
    for i in range(num, 0, -1):
        print(i)

def countdown(num):
    print(num)
    if num > 1:
        countdown(num-1)

countdown(5)