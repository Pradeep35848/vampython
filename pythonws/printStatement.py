# -> # is used to comment the line
# -> it is also used to define the code meaning
# -> it can also comment and uncomment multiple lines using ctrl + /

# comments example
# write a program to print your name 
print("My name is Pawan Sharma") #print function to display statement

#Variables can store the value and it can change at any time 
name = "Pawan Sharma"
#Pass the variable in the print function
print("My name is " + name) # + is used to concatenate the strings

#declare and initialize the multiple variables
age = 33
gender = "male"
#pass the mutiple variable in print function
# this line give the type error 
#Reason for error str can't be concatenate with integer
#Problem 
# print("My name is "+ name + 
#       " my age is "+ age + " and gender is "+ gender)
#Solution 1 - int variable + replace by , 
print("My name is "+ name + 
      " my age is ", age , " and gender is "+ gender)
#Solution 2  - enclosed the variable inside string statement using f
# pass the variable in {} 
print(f"My name is {name} my age is {age} and gender is {gender}")

#Solution 3 - using typecasting
ageInString = str(age)
print("My name is "+ name + 
      " my age is "+ ageInString + " and gender is "+ gender)

#Data types in python
print(type(name)) # type function return datatype of variable
print(type(age)) 
#1. str -> it can store the string data e.g.name = "Pawan sharma"
#2. int -> it can store the numeric data e.g. age = 33
#3. float -> it can store the decimal no e.g. percentage = 75.43

#Typecasting in python:- convert one datatype to another datatypes
#e.g. Sometime when we purchase item in float we paid in integer
purchaseItemPrice  = 90.99
paidItemPrice = int(purchaseItemPrice)
print("Paid amount is", paidItemPrice)

#Note -> string can't be converted into int reason string not ascii

#To get the input from user using input() function
collegeName = input("Enter your college name")
collegeFee  = int(input("Enter your college fee"))
print("My college name is "+ collegeName, collegeFee)
#Note:- the input function has default return type str
#Add scholarship of 25000 in fee
collegeFee = collegeFee - 25000
print("After scholarship my fee", collegeFee)
#Find the age in year when bornYear and currentYear given by user
