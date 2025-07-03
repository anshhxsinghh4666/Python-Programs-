# WAF to find in which line of the file does the word "learning" ocuur first in file practice.txt
# Print -1 if word not found.

def check_for_line(): 
    word = str(input("Enter Word to search:"))
    data = True #For starting iteration or first iteration we keep the condtiton true so that loop can run. If we keep it empty loop will not run.
    line_no = 1
    with open("practice.txt" , "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Found In Line" , line_no)
                return
            line_no+=1
            
    return -1

print(check_for_line())

# CONCEPT:
#       ->Take the word input from user
# let data br true for the loop to start its first iteration.
# start from line_no = 1
# open the file in read mode
# start a while loop : > tell data to read file line by line
#                      > When data become true it will print true. Then return
#                      > Update line no. after every loop
#                      > If can't find word print -1.
    
