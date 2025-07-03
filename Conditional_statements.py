# CONDITIONAL STATEMENTS (if , elif , else)

num=5

if (num>2):
    print("Greater than 2")
if (num>3):
    print("Greater than 3")
#Python always checks "if statement" so it will check both the statements

if (num>2):
    print("Greater than 2")
elif (num>3):
    print("Greater than 3")
# python will first check the "if statement" If it is true then the code will finish
# and if it is false then it will move on to elif statement

# python always checks if statement first 
# Difference between if and elif is that python always check if statement and it will
# only check elif statement only If "if statement" is false 

age=14
if(age>=18):
    print("can vote")
else:
    print("cannot vote")
# If no condition are satisfying then "else statement" is executed
