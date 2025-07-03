# TUPLES : A built in data type that let us create immutable sequences of values. 
#          Parenthesis() are used to make tuples
#          Tuples are similar to list but the difference btw them is that list are mutable and tupels are immutable

tup1=(2 ,1 , 3 , 1)
print(type(tup1))

# TUPLES INDEXING  Note: Similar to Indexing in List or string

print(tup1[0]) #Will return "2"
print(tup1[1])

# tup1[0]=5 : Since tuples are immutable so it will return ERROR

# Empty Tuple : It is a valid tuple
tup2=()
print(type(tup2))
print(tup2)

tup3=(1 , ) #To put a single element in a tuple we need to add a coma after it 
#  like tup3=(1 , ) because if we donot do this and write like tup3=(1) python will read it like an integer
#  and print(type(tup3)) will return <class int> 
print(type(tup3))
print(tup3)

# TUPLES SLICING  Note: Similar to slicing in list or string

tup4=(3 , 9 , 7 , 5 )
print(tup4[1:3])
