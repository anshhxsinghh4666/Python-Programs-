# Indexing
# When a string is written a index is provided to it that is a numbering is given to the characters of the String 
# Numbering starts from 0. For ex:
#         ANSH_    
#         01234    Note: This is positive indexing
# Even special characters are also given a number
# Indexing is used to access a character of a string
# Strings are Immutable , that is we can't change the values of the string. Therefor str[0]=z is not possible as new value can't be assigned to a string as string is immutable


str="Ansh Singh"
ch=str[0]

print(ch)
# OR
print(str[0])

ch2=str[4] #4th character is an empty space so empty space will be printed
print(ch2)

str[2]="z" #Since str are immutable , so we can't change the value of str , therefore it is not possible


# There are two types of indexing 

# Postive Indexing: A P P L E                        Negative indexing: A  P  P  L  E
#                   0 1 2 3 4                                          -5 -4 -3 -2 -1

# Note: Use Negative Indexing only for Slicing
#       Positive Indexing is prefered for Indexing
