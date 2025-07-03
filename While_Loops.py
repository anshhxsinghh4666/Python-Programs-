# LOOPS : Are used to repeat instructions
#         There are two types of loops in Python : While and For loop
#         Loop condtion depends on a variable.


# WHILE LOOP : A "While" Loop is used to repeat a specific block of code an unknown number of times, until a condition is met
#             Syntax:   while condition:
#                           some work


# The Below Code will print "Hello" indefinitely until we break the loop

# while True :
#     print("Hello")  # This will print "Hello" indefinitely until we break the loop

# NOTE: In real life programing we never create infinite loop as it has no practical use and the code written after it will never execute. 

# Print "Hello" 5 times
count = 1  # Iterator (Iterator starting point is 1) (Variable)
# NOTE: 1 is the starting point of the loop. So in variable we store the starting point. So to print hello 5 times starting point is 1 and stopping point is 5 
while count <= 5: # This is a condition to check before loop start (Stopping condition)
# NOTE: 5 is the stopping point for the loop. So with while we write the stopping point. So to print hello 5 times starting point is 1 and stopping point is 5 
    print("Hello")
    count += 1   #This is updation after one Loop iteration. So in 1st Loop count = 1 then afte 1 iteration it will add 1 to count and go on till count becomes 6 (Condition becomes False)
print("Loop Ended")
# This will print "Hello" 5 times . Firstly it will print "Hello" then it will increment count by 1 then again print "hello"
# and this will continue until count becomes 6.

print(count) # This will print 6

# Iterators are the variables used to help in looping through a collection of items. 
# Iteration means running in a Loop until a condition is met.

i = 1 # Iterator (Iterator starting point is 1) (Variable)
while i <= 10:  # (Stopping condition)
    print("Hi" , i) #Will Print "Hello" followed by number from 1 to 10
    i += 1
print("Loop Ended")

# Print numbers from 1 to 5
j = 1 # Iterator (Iterator starting point is 1) (Variable)
while j <= 5:  #Will Print numbers from 1 to 5 (Stopping condition)
    print(j)
    j += 1
print("Loop Ended")

# Print numbers in reverse from 5 to 1
k = 5 # Iterator (Iterator starting point is 5) (Variable) 
while k >= 1:  #Will Print numbers in reverse from 5 to 1 (Stopping condition)
    print(k)
    k -= 1
print("Loop Ended")


# BREAK AND CONTINUE (Part of WHILE LOOP)

# Break : Used to terminate the Loop when encountered.

# Continue : Terminates execution in the current iteration and continues xecution of the loop with the next iteration.

# Break when i=3 (Print from 0 to 3)
i = 0 
while i<=5:
    print(i)
    if (i==3):
        break
    i += 1
print("Loop Ended")

# Continue when i=3 (Print 0 to 5 but skip 3)
i = 0
while i<=5:
    if(i==3):
        i+=1
        continue  #This will skip the current iteration and move to the next iteration. So it will skip 3
    else:
        print(i)
    i+=1
print("Loop Ended")

# OR

i = 0
while i<=5:
    if(i==3):
        i+=1
        continue  #This will skip the current iteration and move to the next iteration. So it will skip 3
    print(i)
    i+=1
print("Loop Ended")

# Print Odd numbers from O to 10
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue  #This will skip the current iteration and move to the next iteration. So it will skip even numbers
    else:
        print(i)
    i+=1   
print("Loop Ended")

# OR

i=1
while i<=10:
    print(i)
    i+=2
print("Loop Ended")

# Print Even numbers from O to 10
i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue  #This will skip the current iteration and move to the next iteration. So it will skip odd numbers
    else:
        print(i)
    i+=1   
print("Loop Ended")

# OR

i=0
while i<=10:
    print(i)
    i+=2
print("Loop Ended")

















