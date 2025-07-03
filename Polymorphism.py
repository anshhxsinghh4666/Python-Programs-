# POLYMORPHISM : 


# OPERATOR OVERLOADING : When the same operator is allowed to have different meanings according to the context.

# Operators & Dunder Functions : 
    # a.__add__(b) : This function is called when the '+' operator is used on two instances of the class.
    # a.__sub__(b) : This function is called when the '-' operator is used on two instances of the class.
    # a.__mul____(b) : This function is called when the '*' operator is used on two instances of the class.
    # a.__truediv____(b) : This function is called when the '/' operator is used on two instances of the class.
    # a.__mod____(b) : This function is called when the '%' operator is used on two instances of the class.
    # a.__gt__(b) : This function is called when the '>' operator is used on two instances of the

# Add 2 Complex numbers :

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(self.real , "i +" , self.imag , "j")

    # Function to add two complex numbers
    def add(self, num2):
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag
        return complex(new_real, new_imag)

num1 = complex(1 , 3)
num1.show_number()

num2 = complex(4 , 6)
num2.show_number()

# Add num1 and num2  
num3 = num1.add(num2)
num3.show_number()
# We can't use num1 + num2 

# So to Fix this check the code bewlow:

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(self.real , "i +" , self.imag , "j")

    # Function to add two complex numbers
    def __add__(self, num2):  # Dunder Function
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag
        return complex(new_real, new_imag)

num1 = complex(1 , 3)
num1.show_number()

num2 = complex(4 , 6)
num2.show_number()

# Add num1 and num2  
num3 = num1 + num2
num3.show_number()


# Substract 2 Complex numbers :
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(self.real , "i +" , self.imag , "j")

    # Function to add two complex numbers
    def __sub__(self, num2):
        new_real = self.real - num2.real
        new_imag = self.imag - num2.imag
        return complex(new_real, new_imag)

num1 = complex(8 , 9)
num1.show_number()

num2 = complex(5 , 1)
num2.show_number()

# Subsatract num1 and num2  
num3 = num1 - num2
num3.show_number()





