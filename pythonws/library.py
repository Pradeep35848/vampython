import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2005, 2006, 2007, 2011, 2026])
grades = np.array([54.05, 72, 69, 73, 71])

#show data in graph- line(x,y),pie(x),      
# bar(x,y),scatters(x,y)
# plt.plot(years, grades, marker = 'o')
# #give the graph title
# plt.title("Academic Growth")
# #set the name for x and y axis
# plt.xlabel("Passing Years")
# plt.ylabel("Student Marks")
# plt.show()
#Note in line,bar,scatters graph 
# the dataset must be same size

trendingLangName = np.array(['Python', 'Javascript', 'Java', 'C#'])
trendingLang = np.array([45, 30, 20,5])
plt.title("Trending Language marketplace")

# plt.pie(trendingLang)
# plt.legend(trendingLangName)
# plt.show()

#Jio 5 years sell growth, 2020 - 2024, 
sales = np.array([200,250, 300, 280, 320])
salesyears = np.array([2020, 2021, 2022, 2023, 2024])

plt.bar(salesyears, sales)
plt.grid()
plt.show()








