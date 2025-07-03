# FILE I/O : Python can be used to perform operations on a file. (Read & Write Data)
#            (I/O stands for input and output)

# Types Of files:
#               -> Text File (contains text data)- .txt , .docx , .log etc.
#               -> Binary File (contains binary data) - .jpg , ,jpeg , .png , .mp4 , .mov etc.



# Open , Read , Close File: We have to open a file before reading and writing.
# NOTE: Default mode is 'r' (read mode) i.e if we donot provide any mode he file will open in read mode.

# ->Open Syntax: open(file_name, mode)
#            file_name : name of the file (with extension) eg. sample.txt
#            mode : mode of operation (read, write, append). r:read mode, w:write mode, a:append mode etc.
#                      > 'r' : opens the file in read mode (default mode)
#                      > 'w' : opens the file for writing , truncation the file first i.e whole file data will be deleted and then you will input fresh data.
#                      > 'x' : creates a new file and open it for writing , it fails if the file already exists.
#                      > 'a' : opens the file for writing , appending to the end of the file if it exist. It does not truncate the file  
#                      > 'b' : opens the file in binary mode
#                      > 't' : opens the file in text mode (default mode)
#                      > '+' : opens the disk file for updating (reading and writing)
#                      > 'r+' : opens for reading and writing. The stream is positioned at the begining of the file. DONOT truncate the file. It overwrites the file.
#                      > 'w+' : open for reading and writing. The file if created if it doesn't exist otherwise it is truncated. The stream is positioned at the begining.
#                      > 'a+' : open for reading and writing. The file is created if it doesn't exist. The stream is positioned at the end of the file. DONOT truncate the file.
# NOTE: We can combine two modes like 'r+b' or "b+" to read and write the file in binary


# -> Read Syntax: file.read()  >Reads Entire file
#                 file.readline() > Reads line by line      
# -> Close Syntax: file.close() 


# READING FROM FILE:

f = open("/Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs/demo_1_(For_File_I_O).txt" , "r")
# OR
# f = open("C:\Users\admin\Desktop\Python Programms\/Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs/demo_1_(For_File_I_O).txt" , "r")
# NOTE: If file demon.txt is in the same file as this python file then we can use open("demo.txt")
#       But If file is in different directory then we need to provide complete path. (Right click on the file and copy file of go to the file and use Shift+Alt+c)
data = f.read()
print(data)
print(type(data))
f.close()
# NOTE: As a good and responsible programmer we should always close the file after using it. If we not do if then anyone can access the data or manipulate it.

# To read particular number of characters.
f = open("/Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs/demo_1_(For_File_I_O).txt" , "r")
data = f.read(5) # read only first 5 characters
print(data)
f.close()

# To read line by line
f = open("/Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs/demo_1_(For_File_I_O).txt" , "r")
line1 = f.readline() # read only first line
print(line1)
line2 = f.readline() # read the next line
print(line2)
f.close()
# NOTE: There will be a blank line after the first line because the line "I am learning Python" has \n at the end in the file and the cde reads it.
#       If we write code to read line 3 and the file doesn't have line 3 it will print a blank space.

# NOTE: If python has already read the file till the end then we can't read more lines and it will print empty space.
f = open("/Users/anshkumarsingh/Desktop/Python Programs//Users/anshkumarsingh/Desktop/Python Programs/demo_1_(For_File_I_O).txt" , "r")
data = f.read()
print(data)
line1 = f.readline() # read only first line
print(line1)
line2 = f.readline() # read the next line
print(line2)
f.close()


# WRITING TO FILE:

# Overwrite All data.
f = open("/Users/anshkumarsingh/Desktop/Python Programs/demo_2_(For_File_I_O).txt" , "w")
f.write("I want to learn java script tomorrow.")
f.close()

# Append Data (Add data in the end)
f = open("/Users/anshkumarsingh/Desktop/Python Programs/demo_2_(For_File_I_O).txt" , "a")
f.write("Then I'll move to ReactJS.") #This line will be added in the same line.
f.write("\nThank you.") #\n will add thanl you in next line.
f.close()

f=open("sample.txt" , "w")
# Since this file didnt exist before so python will create it. This will happen in "w" or "a" mode.

# For furthur code uses
f=open("sample.txt" , "w")
f.write("This is a sample file.")
f.close()

# 'r+' mode :  opens the file for reading and writing. The stream is positioned at the begining of the file. DONOT truncate the file. It overwrites the file.
f = open("sample.txt" , "r+")
f.write("abc")   
# Previously the file was "This is a sample file.". After overwriting it becomes "abcs is a sample file."
# as it overwrites "This" and we got "abcs" in the start.
print(f.read()) # This will print "s is a sample file." beacuse after overwriting the file the stream is at s so it starts reading from s
f.close()

# 'w+' mode: open for reading and writing. The file if created if it doesn't exist otherwise it is truncated. The stream is positioned at the begining.
f = open("sample2.txt" , "w+")
f.write("abc")
f.close()
# The file is created (because it doesn't exist before) and "abc" is written in it. If the file had a data w+ will erase it and write fresh data.

# 'a+' mode:
f = open("sample2.txt" , "a+")
print(f.read()) #This will print blank line because the stream is already at the end in 'a+' mode. 
f.write("pqr") #This will add "pqr" in the end of the file.
f.close()


# WITH SYNTAX:  
#           ->  with open("file_name" , "mode" ) as f:
#               data = operation(like f.read() etc.)
# NOTE: with syntax automatically closes the file so we donot need to write f.close()

with open("/Users/anshkumarsingh/Desktop/Python Programs/demo_2_(For_File_I_O).txt" , "r") as f:
    data = f.read()
    print(data)
# NOTE: Here f is the alias for file "/Users/anshkumarsingh/Desktop/Python Programs/demo_2_(For_File_I_O).txt" i.e all data of file is stored in f.
#       alias occurs when two or more variables refer to the same object in memory. 
#       This means that any changes made through one variable will be reflected when accessing the object through the other variable.
# (In avengers we call hero as iron man or tony stark so two name refers to same person. so they are alias)

with open("sample3.txt" , "w") as f:
    f.write("Hello World!")
# This will print the old data and then edit the file with new data "Hello World!"


# DELETING A FILE: Using the os module
#                  Module(like a code library) is a file written by another programmer that generally has a functions we can use.

import os    # Import the os module
os.remove("sample4.txt") # This will delete the file "sample3.txt


