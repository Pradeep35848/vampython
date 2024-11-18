#function can perform any task 
#it can be reuse, function will return the result

#create function to print the name
def printName():
    print("My name is pawan")
#call function to print the name
printName()
#create function to concatenate fname and lname from user
fname = input("Enter your first name")
lname = input("Enter your last name")
def printFullName(firstname, lastname):
    print(firstname +" "+ lastname)
printFullName(fname, lname)



#creat function area of square

proPrice =int(input("Enter the product price"))
trasportFee = int(input("enter transport fee"))
discountPrice = int(input("Enter discount price"))
tax = int(input("enter the tax"))
def printsquare (t, d, p, ta):
    print((t + p + ta - d))
printsquare(trasportFee, discountPrice, proPrice, tax)