# SET FUNCTIONS

collection = set()  # Empty set

# set.add(element) : Adds an element
collection.add(1)
collection.add(2)
collection.add(2)  # Duplicate value will not be stored by set
collection.add(3)
collection.add("Ansh")  # We can pass a string as it is immutable
collection.add((1, 2, 4))  # We can pass a tuble as it is immutable

# collection.add([1 , 2]) #ERROR: Unhashable type   (Unhashable means values that can be mutated) (Hash value means immutable)
# NOTE: We can't pass a List as it is mutable

print(collection)

# set.remove(element) : Remove an element
collection.remove(1)

print(collection)

# set.clear() : Empties the set   (NOTE: Set obtained after above coding : {2, 3, 'Ansh', (1, 2, 4)} )
print(len(collection))  # We will get 4
collection.clear()  # Will empty the set
print(len(collection))  # We will get 0

# Since accoding to above code our set is empty so let's make a new set

# set.pop() : Removes a random valuecol
collection2 = {"hello", "Ansh", "Python", "Apnacollege"}
print(collection2.pop())  # Will remove any random value
print(collection2.pop())  # Will remove any random value

print(collection2)  # Will get the set after removing 2 random values



set1 = {1, 2, 3}
set2 = {2, 3, 4}

# set1.union(set2) : Combines both set values and returns new (Similar to union sets in maths )
# Will combine both sets and remove the dulicate values or count all duplicate values as one value : {1 , 2 , 3 , 4}
print(set1.union(set2))
print(set1)
print(set2)

# set1.intersetction(set2) : Combines common values and returns new (similar to intersection of sets in maths)
print(set1.intersection(set2))  # Will return common elements {2, 3}
