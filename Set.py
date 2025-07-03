# SETS : It is the collection of unordered (No Indexing) items.
#       Each element in the set must be unique and immutable.

# NOTE:Each element in the set are mutable that is the elements in the set can't change BUT SETS are Mutable because new elements can be added 
# to the set or elements can be removed from a set . Therefore elements in the set can't be modified but elements can be added or removed.
  
#       We can store int , float , str , tuple etc in set which are immutable
#       but we can't store list and dictionary in set because they are mutable.
#       Repeated elements are stored only once in a set.
#       We also start set with {}. Both set and dictionary start with {} but dict have key:value pairs.

collection = {1 , 2 , 2 , 3 , 4 , "Ansh" , "Nehal"} 

print(collection) #NOTE: Python will ignore the duplicate values in the set.
print(type(collection))
print(len(collection)) #Len will not count the duplicate values so it will return 6 instead of 7 because there are two 2.

# Empty set : empty_set=set() 
# NOTE: empty_set={} represents and empty dictionary not set

empty_set=set()
print(type(empty_set))




