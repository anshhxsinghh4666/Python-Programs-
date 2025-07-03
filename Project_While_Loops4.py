# WAP to find the factorial of first n natural numbers

n = int(input("Enter Number of n natural number: "))

fact = 1
# NOTE: We always intialise factorial with 1 because with 0 we will only get 0 because multiplication with 0 is 0   

i = 1
while i <= n:
    fact*=i
    i += 1

print("Factorial =" , fact)          
    
