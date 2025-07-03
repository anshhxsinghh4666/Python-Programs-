# Property Decorator : We use property decorator on any method in the class to use the method as a property.

class student1:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage =  (self.phy + self.chem + self. maths)/3

stud1 = student1(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86   # This will change the marks
print(stud1.phy)
print(stud1.percentage)   # But this will still print the old percentage as the value is not updated in method.

# To fix this check the code below:

class student2:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage =  (self.phy + self.chem + self. maths)/3

    def calc_percentage(self):
        self.percentage =   (self.phy + self.chem + self. maths)/3

stud1 = student2(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86   # This will change the marks
print(stud1.phy)
stud1.calc_percentage()  # This will update the percentage. Now it will print the new percentage.
print(stud1.percentage) 

# OR Using property decorator : (Better method)

class student3:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return   (self.phy + self.chem + self. maths)/3

stud1 = student3(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86   # This will change the marks
print(stud1.percentage)   # This will print the new percentage.