#import matplotlib and name it as plt
import matplotlib.pyplot as plt
#input list of cost
costs=[1,8,15,7,5,14,43,40]
#sort the list
costs.sort()
#print the sorted list
print(costs)

#draw bar plot of sorted costs and label it
x=[1,2,3,4,5,6,7,8]
labels=["Los Angeles 1984","Sydney 2000","Atlanta 1996","Seoul 1988","Athens 2003","Barcelona 1992","London 2012","Beijing 2008"]
plt.xticks(x,labels,rotation=300)
plt.bar(x,costs)
#show the plot
plt.show()
