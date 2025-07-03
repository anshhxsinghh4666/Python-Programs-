# WAP to find average of n numbers

num_val = int(input("Enter number of numbers to find avg: "))

sum = 0
for i in range(1 , num_val+1):
    a = int(input("Enter Number :"))
    sum+=a
avg = sum/num_val
print("Average =", avg)