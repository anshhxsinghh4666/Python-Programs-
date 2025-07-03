# Write a Recursive Funaction to print all elements in a list. (HINT: Use list & index as parameters)

Girls = ["Ajuni" , "Aanya" , "Tisha" , "Nehal" , "Tarini"]

def print_list(list , idx):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list , idx+1) #Recursion Call

print_list(Girls , 0)