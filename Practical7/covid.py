#iport important packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change work dictionary
os.chdir("./")
#print(os.getcwd())
#print(os.listdir())
#import data
covid_data = pd.read_csv("full_data.csv")
#show the second column from every 100th row from the first 1000 rows 
print(covid_data.iloc[0:1001:100,2])
#use a Boolean to show “total cases” for all rows corresponding to Afghanistan
print(covid_data.loc[covid_data.loc[:,"location"]=="Afghanistan","total_cases"])
#compute the mean number of new cases and new deaths on 31 March 2020
new_data=covid_data.loc[covid_data.loc[:,"date"]=="2020-03-31",["location","new_cases","new_deaths"]]
deaths=new_data.loc[:,"new_deaths"]
d=np.mean(deaths)
print(d)
cases=new_data.loc[:,"new_cases"]
c=np.mean(cases)
print(c)
#create boxplot of new cases and new deaths on 31st March 2020
plt.ylabel("number of cases")
plt.xticks(deaths)
plt.xlabel("new deaths in different areas")
plt.title("New deaths on 31st March 2020")
plt.boxplot(deaths,showfliers = False)
plt.show()
plt.ylabel("number of cases")
plt.xticks(cases)
plt.xlabel("new cases in different areas")
plt.title("New cases on 31st March 2020")
plt.boxplot(cases,showfliers = False)
plt.show()
#plot new cases and new deaths worldwide over time
world=covid_data.loc[covid_data.loc[:,"location"]=="World",:]
world_new_cases=world.loc[:,"new_cases"]
world_new_deaths=world.loc[:,"new_deaths"]
world_dates=world.loc[:,"date"]
plt.ylabel("number of cases")
plt.xlabel("date")
plt.title("New cases and new deaths worldwide over time")
plt.plot(world_dates, world_new_cases, 'b+', label="world new cases")
plt.plot(world_dates, world_new_deaths, 'r+',label="world new deaths")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=300)
plt.legend(loc="best",fontsize=12)
plt.show()
#the code answering the question
#show the plot of total cases and new cases in UK to show the development
UK=covid_data.loc[covid_data.loc[:,"location"]=="United Kingdom",:]
UK_total=UK.loc[:,"total_cases"]
UK_new_cases=UK.loc[:,"new_cases"]
UK_date=UK.loc[:,"date"]
plt.ylabel("number of cases")
plt.xlabel("date")
plt.title("Total cases and new cases in UK over time")
plt.plot(UK_date,UK_total,label="total cases")
plt.plot(UK_date,UK_new_cases,label="new cases")
plt.xticks(UK_date.iloc[0:len(UK_date):4],rotation=300)
plt.legend(loc="best")
plt.show()
