# WAF that replaces all occurences of "Java" with "python" in a file practice.txt

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "python") 
print(new_data)  #This will print the updated data of the file but will not edit the file.

with open("practice.txt", "w") as f:
    data = f.write(new_data) #This will overwrite the old data in the file with new data.


# CONCEPT:
# 1. Open the file in read mode (with "r")
# 2. Read the contents of the file into a variable (data)
# 3. Replace all occurrences of "Java" with "python" in the data variable (new_data)
# 4. Print the new data (new_data)
# 5. Open the file in write mode (with "w")
# 6. Write the new data (new_data) back to the file (overwriting the old data)
# 7. Close the file (to free up resources)