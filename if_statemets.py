
print("Hello, what is your age ? ")

movie_rating = int(input())
if movie_rating < 1 or  movie_rating > 117:
    print("You have entered invalid value, please enter your age")
elif movie_rating <= 12:
    print("You can watch 12a movies")
elif movie_rating <= 15:
    print("You are allowed to watch 12+ movies")
elif movie_rating <=18:
    print("You are allow to watch a movie for 15+")
elif movie_rating >= 18:
    print("You are allowed to watch any movie")



