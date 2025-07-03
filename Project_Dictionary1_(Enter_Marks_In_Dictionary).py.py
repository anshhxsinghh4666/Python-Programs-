# WAP to Enter the marks of 3 subjects (Physics, Chemistry, Maths) and store them in a dictionary.

marks = {}

x=int(input("Enter Physics marks: "))
marks.update({"Physics":x})

x=int(input("Enter Chemistry marks: "))
marks.update({"Chemistry":x})

x=int(input("Enter Maths marks: "))
marks.update({"Maths":x})

print(marks)