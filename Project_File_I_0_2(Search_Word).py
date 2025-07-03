# WAF to Search if the word "learning" exist in the file practice.txt

with open("practice.txt", "r") as f:
    data = f.read()
    word = str(input("Enter word to search: "))
    if(word in data):    #OR if(data.find(word) != -1):
        print("FOUND")
    else:
        print("NOT FOUND")


# OR

def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        word = str(input("Enter word to search: "))
        if(word in data):    #OR if(data.find(word) != -1):
            print("FOUND")
        else:
            print("NOT FOUND")

check_for_word()

# Refer String_Funactions.py for info about find() function.