# WAP to print the count of even numbers from the file practice2.txt containing numbers seperated by comma.

count = 0
with open("practice2.txt", "r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")  # this will create a list named nums containing the file data seprated by comma. 
    for val in nums:
        if int(val)%2 == 0:
            count += 1
print(count)

# CONCEPT:
# > Take A initiater count = 0
# > open the file and read it and print the data
# > Convert the data into list nmaed nums using split function
# > type cast the str numbers to int and check if they are even.
# > When found an even number update value of count.  


# OR

# with open("practice2.txt", "r") as f:
#     data = f.read
#     print(data)
#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             print(int(num))
#             num = ""
#         else:
#             num+=data[i]

