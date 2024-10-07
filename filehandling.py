#create file for saving my laptop password
#open function will create the file
#when file is not exists and write the file
myPassword = open("password.txt", "w")

#write my laptop password in file
myPassword.write("my macbook password - guhiguhi")

#overwrite the new password using userinput 
# myPassword.write(input("enter new password"))

#read the password from file
myPassword = open("password.txt", "r")
mydata = myPassword.read()
if "macbook" in mydata:
    print("yes")
else:
    print("No")
#to close the file
myPassword.close()

#delete the file
import os
os.remove("password.txt")

#Create read write delete csv, excel, json, txt
#create csv file
myCsv = open("myfile.csv", "w")
myCsv.write("pawan, tripti, anjali, saloni, suryansh")

myexcel = open("myexcel.xlsx", "w")
myexcel.write("name, pawan, raman, anjali")






