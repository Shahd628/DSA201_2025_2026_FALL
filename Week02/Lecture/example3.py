f = open("movies.txt")

allLines = f.readlines() # returns a list of lines (strings)

f.close()

myMovies = set()

for line in allLines:
    line = line.strip()
    info = line.split(", ")
    currentMovies = info[1:]
    for movie in currentMovies:
        movie = movie.strip()
        myMovies.add(movie)
        """
        if movie not in myMovies:
            myMovies.add(movie)
        """
print("The number of unique movies is", len(myMovies))

for i in range(5):
    if len(myMovies) > 0:
        minMovie = min(myMovies)
        print(minMovie)
        myMovies.remove(minMovie)