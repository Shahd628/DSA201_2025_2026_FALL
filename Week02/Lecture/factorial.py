def calc_fact(n):
    if n == 1: # base condition
        return 1
    return n * calc_fact(n-1)

def calc_fact_without_recursion(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# main
if __name__ == "__main__":
    res = calc_fact(4)
    res2 = calc_fact_without_recursion(4)
    print(res, res2)