# NESTING    (if statement under an if statement)

age=int(input("Enter your Age:"))

if(age>=18):
    if(age>=80):
        print("Cant Drive")
    else:
        print("Can Drive")
else:
    print("Cant Drive")
 
