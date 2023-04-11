#import matplotlib and name it as plt
#input dictionary of cost
#sort the dictionary and make it become a list
#change the list into dictionary
#print this dictionary
#draw bar plot of sorted costs and label it
import matplotlib.pyplot as plt
costs={"Los Angeles 1984":1,"Seoul 1988":8,"Barcelona 1992":15,"Atlanta 1996":7,"Sydney 2000":5,"Athens 2003":14,"Beijing 2008":43,"London 2012":40}
costs=sorted(costs.items(),key=lambda costs:costs[1])
costs=dict(costs)
print(costs)
x=[1,2,3,4,5,6,7,8] #x means the bar in x axis
plt.xticks(x,costs.keys(),rotation=300)
plt.ylabel("Cost (in $ billions)")
plt.bar(x,costs.values())
#show the plot
plt.show()
