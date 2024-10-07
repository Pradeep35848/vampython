#oops in python

#Object oriented programming -> objects

#class -> it is a container which collection variables, functions
#Example -> tripti class
# tripti.fullname = "triptisahu"
# tripti.age = 19
# tripti.sleeping()
# tripti.eating()
# tripti.watching()
#class syntax
class ClassName:
    print("this is my class")

class Pawan:
    age = 33
    fullName = "Pawan Sharma"
    email = "apkglobal0@gmail.com"
    def pocketMoney(this, amount):
        print("My pocket money is", amount)
    def monthlySalary(this, daySalary):
        totalSalary = 31* daySalary
        print("Your monthly salary is", totalSalary)

#create class object
#object:className = ClassName()
pawan:Pawan = Pawan()
pawan.pocketMoney(15000)
pawan.monthlySalary(int(input("Enter your one day salary")))
print(pawan.fullName, pawan.age, pawan.email)
