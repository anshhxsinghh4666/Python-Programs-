# Range : It retuens a sequence of numbers , starting from 0 by default , 
#         increments up by 1 by default and stops before a specfied number.
#         Range works on 3 variables : Start = 0 (By default) (Optional)
#                                      Step = 1  (increment) (By default) (Optional)
#                                      Stop = x   (range(x)) (Compulsary)
# NOTE: Stop is not included.
#       Start is included.

#  Syntax: range(start?, stop, step?)
# NOTE: ? means the parameters are optional. So if we donot write start and step , python will take them as 0 & 1 by default.

seq = range(5)  #range(stop)

#It is not compulsary to store range in a variable like seq = range(5). 

print(range(5))
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
# NOTE: End is not included. So print(seq[5]) will give error.
print("Loop Ended")

for i in seq:  #The Loop stores values of range like 0 , 1 , 2 etc in i
    print(i)  #Since seq = range(5) it will print numbers from 0 to 5
# NOTE: Stop is not included.
print("Loop Ended")

# OR

#It is not compulsary to store range in a variable. Generally we write code like written below.
for i in range(5):  #range(stop)
    print(i)  #Since seq = range(5) it will print numbers from 0 to 5
# NOTE: Stop is not included.
print("Loop Ended")

for i in range(2, 10):  #range(start, stop)
    print(i)
print("Loop Ended")

for i in range(2, 10, 2):  #range(start, stop, step)
    print(i)
print("Loop Ended")

# Print all Even Numbers from 0 to 20
for i in range(2, 21, 2):  #range(start, stop, step)
    print(i)
print("Loop Ended")

# Print all Odd Numbers from 0 to 20
for i in range(1, 20, 2):  #range(start, stop, step)
    print(i)
print("Loop Ended")





