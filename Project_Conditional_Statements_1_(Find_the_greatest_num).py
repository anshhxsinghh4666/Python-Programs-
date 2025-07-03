# FIND THE GREATEST NUMBER : WAP to find the greatest of 3 numbers entered by the user

a=int(input("Enter Num1:"))
b=int(input("Enter Num2:"))
c=int(input("Enter Num3:"))
if (a>b and a>c):
    print("num1 is greatest")
elif (b>a and b>c):
    print("num2 is greatest")
elif (c>b and a<c):
    print("num3 is greatest")
else:
    print("Error:Two or more numbers can't be same")


