#iport important packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change work dictionary
os.chdir("C:/cygwin64/home/86134/IBI1_2022-23/Practical7")
print(os.getcwd())
print(os.listdir())
#import data
covid_data = pd.read_csv("full_data.csv")
#show the second column from every 100th row from the first 1000 rows 
print(covid_data.iloc[0:1001:100,2])
#use a Boolean to show “total cases” for all rows corresponding to Afghanistan
print(covid_data.loc[covid_data.loc[:,"location"]=="Afghanistan","total_cases"])
#compute the mean number of new cases and new deaths on 31 March 2020
new_data=covid_data.loc[covid_data.loc[:,"date"]=="2020-03-31",["location","new_cases","new_deaths"]]
print(new_data)
deaths=new_data.loc[:,"new_deaths"]
d=np.mean(deaths)
print(d)
cases=new_data.loc[:,"new_cases"]
c=np.mean(cases)
print(c)
#create boxplot of new cases and new deaths on 31 March 2020
plt.boxplot(deaths)
plt.show()
plt.boxplot(cases)
plt.show()
#plot new cases and worldwide over time
world=covid_data.loc[covid_data.loc[:,"location"]=="World",:]
world_new_cases=world.loc[:,"new_cases"]
world_dates=world.loc[:,"date"]
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
#plot new deaths worldwide over time
world_new_deaths=world.loc[:,"new_deaths"]
plt.plot(world_dates, world_new_deaths, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
#the code answering the question
#show the plot of total cases and new cases in UK to show the development
UK=covid_data.loc[covid_data.loc[:,"location"]=="United Kingdom",:]
UK_total=UK.loc[:,"total_cases"]
UK_new=UK.loc[:,"new_cases"]
UK_date=UK.loc[:,"date"]
plt.plot(UK_date,UK_total)
plt.plot(UK_date,UK_new)
plt.xticks(UK_date.iloc[0:len(UK_date):4],rotation=-90)
plt.show()
