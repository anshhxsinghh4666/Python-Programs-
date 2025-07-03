# Code to take input of a list
# from the user.

# Take input of the size of the list
n = int(input("Enter number of elements: "))

# Declare an empty list
list = []

# Iterate for n times take inputs
for i in range(n):
    # Take input of ith element as x.
    x = int(input())
    # Append 'x' to the list.
    list.append(x)

# Print the list
print("List:", list)
