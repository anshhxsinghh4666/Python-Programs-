#  WAP to check if a given number is Armstrong number or not

# Aromstrong Number : A number that is equal to the sum of its own digits each raised to the power of the number of digits.
#                     E.g. 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

num = input("Enter a number: ")
len = len(num)

val1 = int(num[0])
val2 = int(num[1])
val3 = int(num[2])

num2 = int(num)
print(type(num2))

sum = val1**len + val2**len + val3**len

if sum == num2:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
