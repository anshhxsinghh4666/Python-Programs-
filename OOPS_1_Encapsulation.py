# ENCAPSULATION : Wrapping data and functions into a single unit (object).

# Making a class containing attributes and methods i.e. puting attributes and methods in an capsule and using it as a object is called encapsulation.

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
