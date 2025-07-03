# LIST SLICING : Accessing parts of List

# list_name[starting_index : ending_index]  Note: Ending index is not included

# marks=[87 , 64 , 33 , 95]
# marks[1:4] is [64 , 33 , 95]
# marks[ :4] is same as [0:4]
# marks[1: ] is same as marks[1:len(marks)]
# marks[-3:-1] is [33 , 95]

# Positive Indexing : [87 , 64 , 33 , 95 , 76]                             Negative Indexing : [87 , 64 , 33 , 95 , 76]
#                      1     2    3    4    5                                                   -5   -4   -3   -2   -1
                                                           


marks=[85 , 94 , 76 , 63 , 48]

# Slicing Using Positive Indexing
print(marks[1:4])  #Ending index is not included
print(marks[ :4])  #Same as [0:4]
print(marks[1: ])  #Same as [1:len(marks)]

#Slicing Using Negative Indexing
print(marks[-4:-1])
