import numpy as np
#import pandas as pd

# #Create an array start from 0 to 49
# # empSalary = np.array([0,1,2,3,4])
# empSalary = np.arange(10)
# 1 * 10
# 10 * 1
# 2  * 5
# 5 * 2

# #find the min, max, mean from empSalary
# print("Mean is",empSalary.mean())
# print("Max is ", empSalary.max())
# print("Min is ", empSalary.min())
# myData = empSalary.reshape(2,5)
# myData = myData + 500
# print("mydata shape is", myData.shape)
# print(myData)
# #Array slicling
# print(empSalary[:])
# emp = np.array([5,6,3,2,1,9,10,4,7,8])
# print(emp[ : -5]) 

# #Pandas will represent the dataset in dataframes
# myDataFrame = pd.DataFrame(data= np.arange(0,50).reshape(10, 5))
# print(myDataFrame)
# print("mean", myDataFrame.mean())
# print("median", myDataFrame.median())
# print("mode", myDataFrame.mode())
# print(myDataFrame.head(1))
# print(myDataFrame.tail())
# print(myDataFrame.loc[[6,]])

#Create an array start from 0 to 49
myData= np.array([0,1,2,3,4])
print(myData)
print("mean", myData.mean())
print("median", myData.max())
print("mode", myData.min())
#print(myData.head(1))
#print(myData.tail())
#print(myData.loc[[6,]])
