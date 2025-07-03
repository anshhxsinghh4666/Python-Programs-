user_dict = {}

num_entries = int(input("Enter the number of entries you want to add: "))

for i in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("Dictionary after adding user input:", user_dict)
