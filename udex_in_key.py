# "in" keyword

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter somethhing you've wathced recently: ")

print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")

else: 
    print("No")
