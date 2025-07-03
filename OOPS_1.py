# OOPS (Part 1) : Object-Oriented Programming System  (Very Important Concept)
#        To map with real wolrd scenarios , we started using objects in code. This is called OOPS.
#        > CLASS : Blueprint for creating objects.
#        > OBJECT : Instance of a class.
# ATTRIBUTES : Data stored inside the class or objects. in the below codes name , marks etc are the attributes.
#              There are two types of attributes: CLass Attributes and Instance Attributes. 
#              (Check my notes for furthur explanation of attributes.)


# Class: Blueprint for creating objects.
class student1:    #Creating a class named student1.
    name = "Ansh Singh"

# Objects: Instance of a class.
s1 = student1()  # Creating an object named s1 from the class student1.
print(s1)
print(s1.name)  # Accessing the attribute of the object. 
s2 = student1()
print(s2.name) # We will again get 'Ansh Singh' as output as it is in the blueprint so its a common attribute of all student1 i.e. all students have same name.


# Class : Blueprint of object car.
class car:
    colour = "BLue"  #Class attribute
    brand = "Mercedes Benz" #Class attribute
    model = "Mercedes Benz Maybach GLS600"  #Class attribute

# Object : Instance of car.
car1 = car()
print(car1.colour)
print(car1.brand) 
print(car1.model)



#__init__ Function (Constructor) : All classes have a function called __init__() (init is short for initialisation) , which is always executed when the object is being initiated.

# Syntax: Creating class  (Constructor)
#           class student:
#              colleg_name = "ABC University"  #Class attribute.
#              def __init__(self, fullname):
#                   self.name = fullname    #Instance attribute.

# Syntax : Creating object
#            s1 = student("Ansh Singh")
#            print(s1.name) 

# NOTE: The self parameter is a reference to the current object (instance of class), and is used to access variables that belong to the class or create new ones.

class student2:
    name = "Ansh Singh"
# NOTE: Always pass self argument in the constructor to initialize the object.
    def __init__(self):  #Output: <__main__.student2 object at 0x00000207E4603B00>   
        print(self)
        print("Adding new student in the database")
# NOTE: It is not neccesary to write self parameter as 'self'. We can name self parameter as abcd etc. But generally, we use 'self' for self parameter.

s1 = student2() #This will call the __init__ function (Constructor) and print the message.
print(s1)  # Output: <__main__.student2 object at 0x000001E54C023C80>
# NOTE: The self variable and s1 variable are pointing each other. 
#       print(s1) and print(self) will give same output because they are refering each other or pointing at each other.

# In the above code name = "Ansh Singh" is a static variable as it is in blueprint so every student is named "Ansh Singh"


# To name every student differently , check the code below:
class student3:
    def __init__(self , fullname):
        self.name = fullname  #(name is the new variable created on class)
        print("Adding new student in the database")

s1 = student3("Ansh Singh")
print(s1.name)  # Output: Ansh Singh

# value assigned in s1 = student3(x) i.e x="Ansh Singh" is stored in fullname. 
# And self.name creats a new variable name in class and value of fullname is assigned to name variable.
# so print(s1.name) will give Output: Ansh Singh

s2 = student3("Nehal Dagar")
print(s2.name) # Output: Nehal Dagar

# NOTE: Constructor is called with every new object. Like in the above code firstly constructor is called for s1 and then s2.


class student4:
    college_name = "ABC University"  #college_name is a Class attribute.
    def __init__(self , name , marks):   #Its not neccesary to write 'fullname' we can write name there as well as with self.name but here self.name creats another variable as before. Generelly we use same variable at both places.
        self.name = name  #(name is the new variable created on class) (different from name variable in statement: def __init__(self , name , marks):)
        self.marks = marks  #(marks is the new variable created on class) (different from marks variable in statement: def __init__(self , name , marks):)
        print("Adding new student in the database")

#Instance Attributes
s1 = student4("Ansh Singh" , 92)
print(s1.name , s1.marks)  # Output: Ansh Singh
s2 = student4("Nehal Dagar" , 82)
print(s2.name , s2.marks) # Output: Nehal Dagar

#Class Attribute
print(s2.college_name) #OR print(s1.college_name) # Output: ABC University
# OR
print(student4.college_name)  # Output: ABC University)

# NOTE: If Class attribute and instance/object attributes are same then object attribute has higher preference (object attr > class attr)


class student5:

#   Default Constructor : If we dont write it python will by default call/write the constructors
    def __init__(self):
        pass

#   Parameterized Constructor : Construtors with parameters other than self too.
    def __init__(self , name , marks):       
        self.name = name  #self.name is an instance attribute.
        self.marks = marks   #self.marks is an instance attribute.
        print("Adding new student in the database")

s1 = student4("Ansh Singh" , 92)
print(s1.name , s1.marks)  # Output: Ansh Singh
s2 = student4("Nehal Dagar" , 82)
print(s2.name , s2.marks) # Output: Nehal Dagar

# NOTE: The constructor which will match the parameter of object like name marks etc will be called. If no match found python will call default constructor.
#       In the above call parameters are matching with def __init__(self , name , marks):  constructor so this will be called and other one will not.




