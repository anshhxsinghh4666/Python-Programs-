# WAF to find the Factorial of n. (HINT: n is a parameter)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    return calc_fact

calc_fact(5)
calc_fact(9)
