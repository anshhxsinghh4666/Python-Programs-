# Search a number x in this tuple using loop:

tup = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 , 49)

x=int(input("Enter a number: "))

idx=0
for i in tup:
    if (i==x):
        print("Number Found in the list at index" , idx)
        break
    else:
        print("Number not found in the list")
    idx+=1
print("Loop Ended")

# NOTE: Since there are two 49 in the tuple the program
#       will print the index of the first occurrence of 49 becaue we used break

# If we want to find all the occurrences of 49 DONOT use break. Check the code below :

idx=0
for i in tup:
    if (i==x):
        print("Number Found in the list at index" , idx)
    else:
        print("Number not found in the list")
    idx+=1
print("Loop Ended")


# Searching X in a list , tuple etc. using the code below is called LINEAR SEARCH
idx=0
for i in tup:
    if (i==x):
        print("Number Found in the list at index" , idx)
    idx+=1
print("Loop Ended")

