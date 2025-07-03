# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to calculate the average marks.

class Student:
    college_name = "ABC University"
    def __init__(self, student_name, name1, marks1, name2, marks2, name3, marks3):
        self.student_name = student_name
        self.name1 = name1
        self.marks1 = marks1
        self.name2 = name2
        self.marks2 = marks2
        self.name3 = name3
        self.marks3 = marks3

    def avg_marks(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print(avg)
        return avg
    
s1 = Student("ANSH SINGH", "Physics", 92, "Chemistry", 88, "Maths", 98)
s1.avg_marks()
print("Avg Marks of", s1.student_name, "is", s1.avg_marks())

# OR

class Student2:
    college_name = "ABC University"
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def avg_marks(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("Avg Marks of", self.student_name, "is", sum/3)

s1 = Student2("ANSH SINGH", [92, 88, 98])
s1.avg_marks()
