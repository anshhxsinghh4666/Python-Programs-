# WAF to print the elements of list in single line.

cities = ["delhi" , "Noida" , "Gurgaon" , "Mumbai" , "Bangalore"]
heroes = ["iron man" , "thor" , "spiderman" , "hulk" ]

print(heroes[0], end=" ")
print(heroes[1])

# OR

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)