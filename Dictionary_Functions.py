# DICTIONARY FUNCTIONS

student = {
    "name" : "Ansh",
    "subjects" : {
        "phy" : 92,
        "chem" : 97,
        "maths" : 95
    }
}

# myDict.keys() : Returns all Keys
print(student.keys())  
# NOTE: It will not return keys of nested dictionary

# To Convert Dictionary to List OR Tuple (We use Type Casting)
print(list(student.keys()))

# To Find Total Number of Keys
print(len(student.keys()))
# OR
print(len(list(student.keys())))
# OR
print(len(student))

# myDict.values() : Return all Values
print(student.values()) 
print(list(student.values())) # (Typecasting to list) Will convert values to list   (In this a dict will store inside a list) 
# NOTE: A list can be stored under a dictionary and vise versa

# myDict.items() : Returns all key:values pairs as tuples
print(student.items())
print(list(student.items())) #Typecasting to list
# Since tuples are converted to list Now indexing is done and now we can access character using index 
pairs=list(student.items())
print(pairs[0])

# mydict.get("key") : Returns the Value stored in key
print(student.get("name"))
# OR
print(student["name"])

# NOTE: Difference between print(student.get("name")) and print(student["name"])
#       that when we put a wrong key in the code then
#       print(student.get("name")) will return "None" and
#       print(student["name"]) will return Error

# Since "name2" donot exist
print(student.get("name2")) # Will return "None"
# OR
# print(student["name2"]) # Will return Error and code after this will note execute

# NOTE: Practically while writting codes we should avoid using codes like print(student["name"]) which can provide error 
# because when once error is occured the code written after the error code will also not execute so we should use functions
# like print(student.get("name")) instead because in case of error it donot provide an error and passes None and due to this 
# the codes written after this can also be executed. Therfore it is advised to use functions.

# myDict.update(newDict) #Inserts the specified items to the dictionary
student.update({"age":20}) #Will add "age:20" to dictionary
# OR
new_dict= {"city":"Delhi" , "Class":12} #Will add  "city":"Delhi" & "Class":12 to dictionary
student.update(new_dict) #Will add  "city":"Delhi" & "Class":12 to dictionary

new_dict2={"name":"Nehal"}
student.update(new_dict2)  #Will UPDATE the name in the dictionary
student.update({"age":18}) #Will UPDATE the age in the dictionary 
# NOTE: If we pass the same key in myDict.update(newDict) , it will not make a new key , it will update the current key because 
#       duplicate keys are not allowed in dictionary

print(student)



