# RANDOM PASSWORD GENERATOR : The pass contains characters from A-Z, a-z, digits, and special characters or punctuators.
#                             Password of length Entered by user.

import random    # random module is used for generating random value.
import string    # string module contains all the string constants

pass_len = int(input("Enter the length of password: "))
val1 = string.ascii_letters + string.digits + string.punctuation 


password = ""
for i in range(pass_len):
    password += random.choice(val1)   #This will add all the random va1ues in the string password.

print("Random Password: ", password) 


# OR (Using List Comprehension)

# List comprehension syntax:    function for i in range(start, stop, step)


pass_list = [random.choice(val1) for i in range(pass_len)]  # This will add all the random values in the list format.
pass_str = "".join(pass_list)  # This will convert the list to string.
print("Random Password: ", pass_str)  # This will print the password.
