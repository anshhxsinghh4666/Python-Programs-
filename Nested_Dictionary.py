# NESTED DICTIONARY

student = {
    "name" : "Ansh",
    "subjects" : {
        "phy" : 92,
        "chem" : 97,
        "maths" : 95
    }
}
print(student)
print(student["subjects"]) #Will print marks in all subjects
print(student["subjects"]["chem"]) #Will print marks in chem
