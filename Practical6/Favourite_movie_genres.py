#import matplotlib and name it as ptl
import matplotlib.pyplot as ptl
#input the keys and values of dictionary "movie"
movie={"Comedy":73,"Action":42,"Romance":38,"Fantasy":28,"Science-fiction":22,"Horror":19,"Crime":18,"Documentary":12,"History":8,"War":7}
#print the dictionary
print(movie)
#draw pie plot using values in movie
ptl.pie(x=movie.values(),labels=movie.keys())
#show this plot
ptl.show()
# HERE: user can change the preferred genre:
requested_genre="Comedy"
#find the number that pairs with "requested_genre" and output as a sentence
output="The number of students who likes "+requested_genre+" is "+str(movie[requested_genre])
print(output)
