# NON STATIC METHODS : Methods are functions that belong to objects.
#           OR we can say Functions under class are called methods.

# SYNTAX:     class student:
    #             def __init__(self, name, age):
    #                 self.name = name
    #                 self.age = age

    #             def hello(self):
    #                 print("Hello" , self.name)

    # s1 = student("Ansh Singh", 20)
    # s1.hello()

class student:
    college_name = "ABC University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # Method to welcome the student
    def welcome(self):
        print("Welcome Student" , self.name)

    # Method to get the marks
    def get_marks(self):
        return self.marks

s1 = student("Ansh Singh", 92)
s1.welcome()
print(s1.get_marks())

s1.name = "Nehal Dagar"  #We can edit the name attribute.
s1.welcome()
print(s1.get_marks())



