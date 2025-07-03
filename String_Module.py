# STRING MODULE: Python provides the string module that contains all the string constants

import string    # string module contains all the string constants

val1 = string.ascii_letters   # will print all alphabets in both upper and lower case
print(val1)  
print(type(val1))  #Output : <class'str'>

val2 = string.ascii_lowercase   # will print all lowercase alphabets
print(val2)

val3 = string.ascii_uppercase   # will print all uppercase alphabets
print(val3)

val4 = string.digits   # will print all digits
print(val4)

val5 = string.punctuation   # will print all special characters
print(val5)


# NOTE: ascii stands for American Standard Code for Information Interchange.