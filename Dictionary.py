# DICTIONARY : Dictionaries are used to store data values in Key:value pairs
#              They are unordered , mutable and don't allow duplicate keys

# dict = {
#     "Name": "Ansh",          NOTE: In this line Key is "Name" and value is "Ansh"
#     "Age": 22,
#     "City": "Delhi"
# }

info = {
#   "key" : "Value"
    "Name": "Ansh",
    "Age": 22,
    "City": "Delhi",
    "Subjects" : ["Python" , "C++" , "Java"],  #Value is in form of list
    "Marks": 82.2
        
    
}

print(info)
print(type(info))

# NOTE: All types of datatypes like list , tuple , dictionary , string etc. are accceptable in Value , 
#       But datatypes like list , tuple , dictionary are NOT acceptable in Keys.
#       Keys can be string , integer , float etc. Generally str are used as Keys

# To Access Value in Dictionary
# print(dict["name"]) , print(dict["cgpa"]) etc.

print(info["Name"])
print(info["Age"])
print(info["City"])
print(info["Subjects"])

# To Assign new value 
info["Name"] = "Nehal"
print(info)

# To add a New Key:value pair
info["Surname"] = "Dagar"
print(info)

# Empty Dictionary
null_dict={}
null_dict["Name"] = "Ansh" #We can ad values to empty dictionary
print(null_dict) 



