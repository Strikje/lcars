currentMovies = {
  "The Grinch":"11:00 uur"
    ,"Rudolph":"13:00 uur"
    ,"Frosty the snowman":"15:00 uur"
    ,"Christmas vacation":"17:00 uur"
    }

print("We're currently showing the following movies:\n")

for key in currentMovies:
  print(key)
    
movie = input("What movie do you want the showtime for? ")

showtime = currentMovies.get(movie)

if showtime == None:
  print("The movie isn't showing.")
else:
  print("The movie",movie,"is running at",showtime)