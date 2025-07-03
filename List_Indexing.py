# LISTS  : A built in datatype that stores set of values
#          It can store elements of different data types (int , float , str) together
#          List are Mutable , that is we can change the value in a list
#          Square brackets are used to make List

marks=[94.4 , 87.5 , 95.2 , 66.4 , 45.1]  #list of marks of students     
                                          #list also have index number similar to strings  
    
    # LIST INDEXING
    
    #   [94.4 , 87.5 , 95.2 , 66.4 , 45.1]   
    #      0      1      2      3      4

print(marks)
print(type(marks)) #type of marks

print(len(marks)) #len of list
# NOTE: List index starts from 0 and goes on till len(list)-1

# to access character of list
print(marks[0])    #marks having index[0]
print(marks[2])    #marks having index[2]
print(marks[5])  #Error will occur as index is out of range

student=["Ansh" , 92.2 , 18 , "Delhi"]  #["Name of student" , marks , age , Location]  So we can store different data types (int , float , str) together
print(student)
print(student[0]) #To access name of student
student[0]="karan" #Change name from "Ansh" to "Karan"
print(student) #New list with name karan will be printed

# NOTE: List index starts from 0 and goes on till len(list)-1






