# WAP To Find the factorial of n natural number 

n = int(input("Enter n natural number:"))

fact = 1
for i in range(1, n+1):  # Values from 1 to n are stored in i
# Since stop value is n+1, it will include n in the factorial because stop is excluded in Range
    fact *= i
print("Factorial = " , fact)