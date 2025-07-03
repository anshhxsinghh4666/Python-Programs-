# Define a Employee class with attributes role, department & salary. This class also has a show_details() method.
# Create an engineer class that inherits properties from the Employee & has additional attributes : name & age.   

class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def display_employee_details1(self):
        print(f"Role: {self.role}\n Department: {self.department}\n Salary: {self.salary}")
# NOTE: OR we can use print("Role:" (self.role), "Department": (self.department), "Salary:" (self.salary))

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 100000000)

    def display_employee_details2(self):
        print(f"Name: {self.name}\nAge: {self.age}")

e1 = engineer("Ansh Singh", 23)
print(e1.display_employee_details2())
print(e1.display_employee_details1())
