# CHECK IF LIST CONTAINS A PALINDROME  [HINT : Use copy() method]

# NOTE:Plindrome is  a word, sentence, verse,
# or even number that reads the same backward or forward. Eg: Ma'am , 1 , 11 etc.

list1=[1 , 2 , 1]

copy_list1 = list1.copy()   #list1.copy() makes copy of the original list
copy_list1.reverse()

if(copy_list1 == list1):
    print("List1 is a palindrome")
else:
    print("Not Palindrome")
    

list2=[1 , 2 , 3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("list2 is a palindrome")
else:
    print("Not Palindrome")
    

