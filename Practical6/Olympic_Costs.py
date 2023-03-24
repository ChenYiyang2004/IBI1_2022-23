#import matplotlib and name it as plt
import matplotlib.pyplot as plt
#input dictionary of cost
costs={"Los Angeles 1984":1,"Seoul 1988":8,"Barcelona 1992":15,"Atlanta 1996":7,"Sydney 2000":5,"Athens 2003":14,"Beijing 2008":43,"London 2012":40}
#sort the dictionary and make it become a list
costs=sorted(costs.items(),key=lambda costs:costs[1])
#change the list into dictionary
costs=dict(costs)
#print this dictionary
print(costs)

#draw bar plot of sorted costs and label it
x=[1,2,3,4,5,6,7,8] #x means the bar in x axis
plt.xticks(x,costs.keys(),rotation=300)
plt.bar(x,costs.values())
#show the plot
plt.show()
