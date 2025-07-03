# OOPS (Part 2) : Object-Oriented Programming System  (Very Important Concept)



# del Keyword : Used to delete objrct properties or object itself.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = student("Ansh Singh", 92)
print(s1.name, s1.marks) 
print(s1)

del s1.name
# print(s1.name) -> Error: 'student' object has no attribute 'name'
del s1
# print(s1) -> Error: name 's1' is not defined


# Private (like) attributes & Methods: Private attribites and methods are ment to be used only within the class and are not accessible from outside the class. 

# Syntax: def __init__(self, acc_pass):
#           self.__acc_pass = acc_pass -> Use 2 underscores(__) in methods and attributes after self. like self.__acc_pass or 2 underscore before attribute like __name to make it a private attribute. 

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Private attribute

    def reset_pass(self):
        print(self.__acc_pass)  # Here we can print(self.__acc_pass) even though its a pvt attribute  because it is in class , but can't do this outside of class (Check below). 

acc1 = account("12345", "abcd")
print(acc1.acc_no)

# print(acc1.__acc_pass)  # Can't Access acc_pass outside the class as it is a private attribute.
# Error : 'account' object has no attribute '__acc_pass'

print(acc1.reset_pass())  # we can access acc_pass by calling reset_pass() method because it's in the class.


class person:
    __name = "Ansh Singh"  # Private attribute

    def __hello(self):  # Private method
        print("Hello Person") 

    def welcome(self):  # Funaction inisde class to access private method __hello(self)
        self.__hello    #Private attribute can be called in class. So now we can call welcome() method to print "Hello Person".

p1 = person()
# print(p1.__name)   # Error: 'person' object has no attribute '__name'
# print(p1.__hello())  # Error: 'person' object has no attribute '__hello' 

print(p1.welcome())  # This will call the internal class function welcome which will indirectly call the private method __hello.

# Conclusions: If we make an attribute private using double underscore than only internal function of class can access them .
#              Then to access the private attribute outside the class we need to access them through the function that accessed them inside the class. 



# INHERITANCE : When one class (Child) derives the properties and methods of another class (parent). similiar to one child derives properties of parent.

class car:      # Parent class
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped!")

class bmwcar(car):      # Child Class
    def __init__(self , name):
        self.name = name

car1 = bmwcar("x7 mcomp")
car2 = bmwcar("x5 mcomp")

print(car1.name)

print(car1.start())   # car1 donot have start/stop method so it's inherited from parent class car.
print(car1.stop())
print(car1.color)  # This will give "black" as it is inherited from parent class car.


# TYPES OF INHERITANCE: 
    # 1. Single Inheritance : Child class inherits from one parent class.
    # 2. Multilevel Inheritance : Child class inherits from multiple parent classes which in turn inherit from more parent classes.
    # 3. Multiple Inheritance : Child class inherits from multiple parent classes.
    # 4. Hierarchical Inheritance : Child class inherits from multiple parent classes which in turn inherit from each other.

# Single Inheritance:

class car:      # Parent class
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped!")

class bmw2car(car):      # Child Class
    def __init__(self , name):
        self.name = name

car1 = bmw2car("x7 mcomp")
car2 = bmw2car("x5 mcomp")

print(car1.name)

print(car1.start())   # car1 donot have start/stop method so it's inherited from parent class car.
print(car1.stop())
print(car1.color)


# Multilevel Inheritance :
class car:      # Parent class
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped!")

class LandRover(car):      # Child Class
    def __init__(self , brand):
        self.brand = brand

class Defender(LandRover):  # Child Class of LandRover
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

car1 = Defender("Petrol V8")
print(car1.fuel_type)
car1.start()


# Multiple Inheritance :

class A:    # Parent class 1
    varA = "Welcome to class A"

class B:    # Parent class 2
    varB = "Welcome to class B"

class C(A, B):      # Child Class
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varA)
print(c1.varB)


# Super Method : super() method is used to access methods of the parent class.

class car:      # Parent class
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type    

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped!")

class Lexuscar(car):      # Child Class
    def __init__(self , name , fuel_type):
        self.name = name
        super().__init__(fuel_type)  # Calling parent class constructor for fuel_type. Because in the parent class fuel_type value was not passed.
        super().start()  # Calling parent class start method. So this will start car just after creating car1.

car1 = Lexuscar("LC500" , "Petrol")
print(car1.fuel_type)

