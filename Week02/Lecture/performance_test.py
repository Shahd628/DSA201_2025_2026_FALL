import factorial, time, math
#import time

if __name__ == "__main__":
    start = time.time()
    
    for i in range(1000000):
        res = factorial.calc_fact(100)
    
    end = time.time()
    time_diff = end - start
    print("Recursive:", time_diff)

    start = time.time()
    
    for i in range(1000000):
        res = factorial.calc_fact_without_recursion(100)
    
    end = time.time()
    time_diff = end - start
    print("Iterative:", time_diff)

    start = time.time()
    
    for i in range(1000000):
        res = math.factorial(100)
    
    end = time.time()
    time_diff = end - start
    print("Math Module:", time_diff)