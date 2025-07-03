# LIST Funtions 

list1=[2 , 5 , 1 , 3 , 1]
list2=["Banana" , "Lichi" , "Apple"]

# DOUBT: print(list.append()) should return "None" but due to some error this code is printing "None" as well as appending the same value again at the end.
# For ex. list1.append(5) is print "None" as well as [2 , 1 , 3 , 4 , 4] but it should be printing [2 , 1 , 3 , 4]


# list.append(x) : adds one element at the end
list1.append(5) #Will add 4 in the end
list2.append("Mango") #Will add "Mango" in the end 
print(list1.append(5)) #This will return "None" as it only appends the value
print(list2.append("Mango")) #This will return "None" as it only appends the value
print(list1) #But print(list1) will now return the list1 with value 4 appended in the end
print(list2) #But print(list1) will now return the list1 with value "Mango" appended in the end
# Note: It is also called mutation of list1

# list.sort() : Sorts in Ascending Order
list1.sort()
list2.sort()
print(list1.sort()) #This will return "None" as it only make changes to the list1
print(list2.sort()) #This will return "None" as it only make changes to the list2
print(list1) # But print(list1) will now return the sorted list1
print(list2) # But print(list2) will now return the sorted list2

# list.sort(reverse=True) : Sorts in is Descending Order (Note: In this code true should be written with capital "T")
list1.sort(reverse=True)
list2.sort(reverse=True) 
print(list1.sort(reverse=True))  #This will return "None" as it only make changes to the list1
print(list2.sort(reverse=True))  #This will return "None" as it only make changes to the list2
print(list1) # But print(list2) will now return the sorted list1
print(list2) # But print(list2) will now return the sorted list2

# list.reverse() : Reverse List 
list1.reverse()
list2.reverse()
print(list1)
print(list2)
# Note: Since in the previous code list is sorted in decending order , this list.reverse() will reverse the sorted list
# Otherwise it will reverse the original list that is list1=[2 , 1 , 3] or list2=["Banana" , "Lichi" , "Apple"]

# list.insert(index , element) : Insert element at index
# Note: It is similar to list.append() but add element at a particular index
list1.insert(1 , 5) #Will add 5 at index 1
list2.insert(1 , "Cherry") #Will add "Cherry" at index 1
print(list1)
print(list2)

# list.remove(x) : To remove the first occurance of elemrnt ("x" is the element to be removed , not the index of the element)
# List muatated by the above written code are : list1=[1, 5, 1, 2, 3, 5, 5, 5]
#                                               list2=['Apple', 'Cherry', 'Banana', 'Lichi', 'Mango', 'Mango']
# Therefore the furthur mutation will be done on the basis of the above mentioned list mutated befor

list1.remove(1) #Will Remove the first 1 occuring in the list. So only one 1 which is occuring first will be removed 
list2.remove("Lichi") 
print(list1)
print(list2)

# list.pop(index) : Removes element at a particular index
list1.pop(3)
list2.pop(1)
print(list1)
print(list2)






