# ADD ITEMS TO THE LIST : WAP to ask the user to enter names 
#                         of their 3 favorite movies and store them in a list

Movie1=str(input("Enter Fav Movie1:"))
Movie2=str(input("Enter Fav Movie2:"))
Movie3=str(input("Enter Fav Movie3:"))
list=[]
list.append(Movie1)
list.append(Movie2)
list.append(Movie3)
print(list)

# OR 

movies=[]
movies.append(str(input("Enter Fav movie1:")))
movies.append(str(input("Enter Fav movie2:")))
movies.append(str(input("Enter Fav movie3:")))
print(movies)
