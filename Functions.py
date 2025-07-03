# FUNCTIONS : Block of statements that performs a specific task.
#             Block of code that takes and input and returns and output.
# NOTE: A code in which part of code with same concept is repeating again and again then this is called Redandant Code.
#       Redundancy is not a problem, but it makes the code harder to read and maintain so this type of code is conidered a bad code.
#       Programmer writing redandant code is not a good programmer.
#       So to reduce redundancy we use functions. Whenever redundancy occurs we convert code into a function.

# Syntax: Function defination:
#                def function_name(parameter1 , parameter2 ...):   NOTE:There can be more than 2 parameters.
#                Body of the function (some works)
#                return value

# Function Call:
#        function_name(argument1 , argument2)  #arguments are passed to the function.

# NOTE: Parameters are the variables which are passed to the function.
#       Arguments are the values that are passed to the Parameters in the function.
#       If we donot call the function then the function will not execute i.e they wont print or do anything.


# Function Defination
def calc_sum1(a , b):  #Parameters (a , b)
    sum = a+b
    print(sum)      
    return sum    # this line is used to return the output.
# NOTE: If we donot use return keyword then the function will not return any value.

# Function Call:
calc_sum1(10, 20)  #Arguments (10 , 20)  

# OR

# Function Defination
def calc_sum2(a , b):  # Parameters (a , b)
    return a+b  # this line is used to return the sum/output.

# Function Call:
sum = calc_sum2(10, 20)  #Arguments (10 , 20)
print(sum)

# NOTE: In the type of code above we need to store the Function call in a variable like sum.



# def is a keyword which defines a function.
# calc_sum is the name of the function.
# return keyword is used to return a value from a function.

# We can make a function which donot require and parameter i.e donot take inputs. And we can make a function which donot return any value i.e donot give any output.
# For that type of function check the code below:
def print_hello():
    print("Hello")
    
print_hello()  # Calling the function.
print_hello()

output = print_hello()
print(output)  #None
# It will print None becaue this function donot give any value in return i.e donot give any output.


# There are two types of functions:   
#                               -> BUILT-IN FUNCTIONS
#                               -> USER-DEFINED FUNCTIONS

# BUILT-IN FUNCTIONS: These are functions provided by Python.
#                 -> Print()
#                 -> len()
#                 -> type()
#                 -> Range()
#                 -> etc.........

# # print() function defination : 
#                     def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False
# ) -> None

#   -> sep: " " (Default value is space) : This is used to separate the values printed.
#   -> end: "\n" (Default value is newline) : This is used to add newline.

print("Ansh","Kumar") #sep = " "
print("Singh") #end = "\n"

print("apnacollege", end=" ") 
print("shradhakhappra") #end = " "
# Now Both values be in the same line.

print("Ansh","Kumar", sep="$") #sep = "$"
print("Singh") #end = "\n"

print("Ansh","Kumar", sep="$", end="@") #sep = "$"
print("Singh") #end = "@"


# len() function defination : 
#                 def len(
#     obj: Sized,
#     /
# ) -> int


# USER DEFINED FUNCTIONS: These are functions defined by programmer.



# DEFAULT PARAMETERS :  Assigning a default value to parameter , which is used when no argument is passed.

# def calc_prod(a , b)
#     prod=a*b
#     print(prod)
#     return prod

# calc_prod()  -> Error: SInce no parameter is passed

# To avoid this error we need to pass a default vale to a and b parameters.

def calc_prod(a=1 , b=1):  #Default values are provide to a and b i.e 1
    prod=a*b
    print(prod)
    return prod

calc_prod()  #Since no parameters are passed it will consider the default values.
# -> 1 * 1 = 1

def calc_prod(a=4 , b=2): #Default values of a and b are 4 and 2 resp.
    prod=a*b
    print(prod)
    return prod

calc_prod() # -> 4 * 2 = 8

def calc_prod(a , b=2): #Default value of b is 2. a has no default value.
    prod=a*b
    print(prod)
    return prod

calc_prod(4) #4 will be assigned to a and dafault value of b will be taken.
# -> 4 * 2 = 8

# def calc_prod(a=2 , b):
#     prod=a*b
#     print(prod)
#     return prod

# calc_prod()  

# SyntaxError: Parameter without a default follows parameter with a default
# Therfore always start assigning default vales from the last because last value shouldn't be non default. 




