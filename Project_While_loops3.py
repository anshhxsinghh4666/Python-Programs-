# WAP to find the sum of first n natural numbers

n = int(input("Enter Number of n natural number: "))

sum = 0

i = 1
while i <= n:
    sum+=i
    i += 1

print("Total sum =" , sum)
    
