# Slicing : Accessing parts of string

# str[starting_index : ending_index]  Note:Ending index is not included

# str="Ansh Singh"
# so str[1:4] is "nsh"  
#    str[ :4] is same as str[0:4]
#    str[1: ] is same as str[1:len(str)]

# Postive Indexing: A P P L E                        Negative indexing: A  P  P  L  E
#                   0 1 2 3 4                                          -5 -4 -3 -2 -1


str="Ansh Singh"                                                                                #   A n s h   S i n g h
                                                                                                #   0 1 2 3 4 5 6 7 8 9

#Using Positive Indexing                                                                            
slice1=str[1:4] #donot iclude ending index                                                         
slice2=str[4:8] #donot include nedig index
print(slice1) #OR print(str[1:4])
print(slice2)
print(str[2:len(str)]) #this means slice from index 2 to last index
                       # OR ca n be written as print(str[2:9])
                       #NOTE: It includes the ending index too.
print(str[2:]) #this means that ending index is the last index that is 9
               #OR print(str[2:len(str)])
print(str[:7]) #this means that starting index is 0
               #OR print(str[0:7])                      

# Using Negative Indexing                                                                           
                                                                                            #         A  n  s  h     S  i  n  g  h   
slice3=str[-4:-1]                                                                           #        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(slice3)  

