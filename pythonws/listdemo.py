#list can store multiple data, data can be different types int str
#list can store the duplicate data
#list is an ordered data set - sorting asending descending

#create list and store the your friends name
friendList = ["ivan", "anshu", "anjali", "wani"]
#print the list of friend names
print(friendList)
#add the age of your friends into list
#append will add the data into end of the list
friendList.append(36)
friendList.append(26)
friendList.append(29)
friendList.append(5)

#Add the data into list using index no
friendList.insert(0, "Ayush")
print(friendList)

#to access the data using index no
# print(friendList[2])

# to delete the data from list
#remove will delete the data using value
friendList.remove("ivan")
print(friendList)

#pop will delete the data using index
friendList.pop(3)
print(friendList)


#access the complete list
# for name in friendList:
#     print(name)
#friendList.sort()
#add the 5 favt city name in list
#add my favt city kasol in index 0
#remove the last city in list - using pop
#sorting the list data
#print the list data

favtCity = ["Chandighar", "Manali", "Goa", "Pune", "Assam"]
favtCity.insert(0, "Kasol")
favtCity.pop()
favtCity.sort()
print(favtCity)

