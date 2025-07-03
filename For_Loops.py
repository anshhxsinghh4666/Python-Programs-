# LOOPS : Are used to repeat instructions
#         There are two types of loops in Python : While and For loop
#         Loop condtion depends on a variable.

# FOR LOOP : A "For" Loop is used to repeat a specific block of code a known number of times. Used for sequential trasversal. For traversing list , tuples etc 
#           Syntax : for el in list:
#                       some work         
# NOTE: el is an variable that takes on the value of each item in the list.
#       in is a keyword that is used to iterate over a sequence.


# LIST
list = [1 , 2 , 3 , 4 , 5]
for i in list:
    print(i)    #Will print all the elements in the list
print("Loop Ended")

# TUPLE
tup = (1 , 2 , 3 , 4 , 5)
for i in tup:
    print(i)
print("Loop Ended")

# STRNGS
str = "Hello World"
for i in str:
    print(i)
print("Loop Ended")

# FOR Loop with else 
str = "Hello World"
for i in str:
    print(i)
else:
    print("Loop Ended")
# For loop with else is not compulsarily required in the above code

# But For loop with else is compulsarily required when we use break. Check the code written below:

# Find a charachter in a string
str = "Hello World"
for i in str:
    if(i=='o'):
        print("O Found")
        break     # This will break the loop when 'o' is found and print "O Found" but if not then it will print the else statement
    print(i)
else:
    print("Loop Ended")
# In the above code if we didn't used else then "Loop Ended" will be printed even if we found 'o' or not 
# In the above code else part is not executed because 'o' is found in the string.
# But if 'o' was not found in the string then else part will be executed. Check the code below to find j in the string and else part gets executed:
str = "Hello World"
for i in str:

    if(i=='j'):
        print("O Found")
        break     # This will break the loop when 'o' is found and print "O Found" but if not then it will print the else statement
    print(i)
else:
    print("Loop Ended")
# Therfore else statement will not be executed if break condition become true. It will only execute when break condition is not true till the end of the loop.


