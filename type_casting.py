# TYPE CASTING
val1 = int(input("Enter val1:"))
val2 = int(input("Enter val2:"))
sum = val1 + val2
print(sum)

print(float(9))  # Will typecast (convert) int to float

# # if  we donot use int then
# val1=(input("Enter val1:"))
# val2=(input("Enter val2:"))
# sum=(val1+val2)
# print(sum)
# on running lets put val1=20 and val2=22
# then we will get the sum 2022 because input converts every value into str even int , float etc
# so 20 and 22 are treated as str and there sum become 2022
# therefore we use int to convert str to int
# and this is called TYPE CASTING
