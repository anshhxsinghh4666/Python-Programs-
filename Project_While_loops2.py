# WAP to search a number x in this tuple using loop :
#       (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)


tup = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

x = int(input("Enter the number to search: "))

idx=0
while idx<len(tup):
    if (tup[idx] == x):
        print("Number Found at Index" , idx)
        break
    else:
        print("Finding...")
    idx += 1
print("Loop Ended")
