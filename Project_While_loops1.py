# WAP to Print the elements of the following list using a loop:
#         [1 , 4 , 9 , 16 , 25  36 , 49 , 64 , 81 , 100]


i = 1
j = 1
while i <= 10:
    while j <= 10:
        print(i*j)
        i+=1
        j+=1
print("Loop Ended")

# OR

k=1
while k<=10:
    print(k*k)
    k+=1
print("Loop Ended")

# OR

list = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
# NOTE: List index starts from 0 and goes on till len(list)-1

#  In this code Index is our variable.

idx = 0  # Iterator (Iterator starting point is 0) (Variable)
while idx<len(list):   #OR: while idx<len(list)-1:   # (Stopping condition)
    print(list[idx])
    idx+=1
print("Loop Ended")



















