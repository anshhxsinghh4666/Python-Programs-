# STATIC METHOD (Decorator) : Methods that don't use the self prameter. 
#                  They Works at Class level.

# NOTE: Static Method can't access or modify class state & generally for utility.

# SYNTAX:
#       class Student:
#           @staticmethod      #decorator
#           def college():
#               print("ABC University")

# Decorator : Decorator allows us to wrap another funaction in order to extend the behaviour of the wrapped function ,
#             without permanently modifying it. 

class Student:
    @staticmethod      # No attributes in the funaction.
    def hello():        #NO Need to write self
        print("Hello")

s1 = Student()
s1.hello()


# NOTE: We uses staticmethod when class and instance attributes are not using.
