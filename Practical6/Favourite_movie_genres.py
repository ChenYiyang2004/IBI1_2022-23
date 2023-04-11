#import matplotlib and name it as ptl
#input the keys and values of dictionary "movie"
#print the dictionary
#draw pie plot using values in movie
#show this plot
#find the number that pairs with "requested_genre" and output as a sentence
import matplotlib.pyplot as ptl
movie={"Comedy":73,"Action":42,"Romance":38,"Fantasy":28,"Science-fiction":22,"Horror":19,"Crime":18,"Documentary":12,"History":8,"War":7}
print(movie)
ptl.pie(x=movie.values(),labels=movie.keys())
ptl.show()
# HERE: user can change the preferred genre:
requested_genre="Comedy"
output="The number of students who likes "+requested_genre+" is "+str(movie[requested_genre])
print(output)
