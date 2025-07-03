# WAP to find the sum of first n natural numbers 

n = int(input("Enter Number of n natural number: "))

sum = 0
for i in range(1, n+1):   # Values from 1 to n are stored in i
#Since stop value is n+1, it will include n in the sum because range function excludes the stop value
    sum+=i

print("Total sum =" , sum)




