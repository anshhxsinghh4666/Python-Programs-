# STRING FUNCTIONS

str="i am studying python from ApnaCollege"

# str.endswith("x") : returns true if string ends with the substring  ("x" is the substring )
print(str.endswith("ege")) #true
print(str.endswith("ish")) #false

# str.capitalize() : capitalizes the 1st character                           
print(str.capitalize()) #Note: It forms a new string with 1st capital character and donot modify the original string 
print(str)              # So if we print(str) the old string will be printed that is "i am Ansh"

#To modify the original string
str=str.capitalize() #This will modify the original string.
print(str) 

#str.replace(old , new) : replaces all old occurances of old value to new value
print(str.replace("o" , "a"))  #Will replace o to a
print(str.replace("python" , "Java"))  #will replace python to java

# str.find(word) : returns 1st index of 1st occurrer
print(str.find("o")) #It will the return the index of 1st o occuring in str
print(str.find("from")) #It will return the index of the first letter or the word 
str2="i am from studying python from ApnaCollege"
print(str2.find("from")) #Since there are 2 "from" so ut will return the index of the 1st letter of 1st "from"
print(str2.find("z")) #if the word is not in the str it will show -1
 
# str.count(word) : counts the occurrences of the substring that is no. of times a substring is occurring in a string
print(str2.count("from"))
print(str2.count("o"))
