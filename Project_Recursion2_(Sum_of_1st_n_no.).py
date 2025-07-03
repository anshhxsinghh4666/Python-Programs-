# Write a Recursive Function to calculate the sum of first n Natural Numbers.

def sum(n):
    if (n==0):
        return 0
    else:
        return n+sum(n-1)
    
print(sum(5))  # -> 15

# Refer Project_Recursion1_(Factorial).py 