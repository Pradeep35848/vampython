#For loop is used to no of iteration 

userName = "Pawan Sharma"
for i in userName:
    print(i)

#Print 1 to 10 using for loop
# for(int i=1; i<11; i++)
for x in range(1, 11):
    print(x)

#WAP to create table of any no
# tableNo = int(input("Enter no for create table"))
# for a in range(1, 11):
#     print((a * tableNo))

#WAP to print even no from 1 to 10 using for loop
for a in range(1, 11):
    if a % 2 == 0:
        print(a)

#WAP print this pattern 1 4 7 10 13 using for loop
for y in range(1, 14, 3):
    print(y)

#WAP print this pattern 1 3 7 11 13 15 using for 
for b in range(1,16,2):
    if b == 9 or b == 5:
        continue #skip the current iteration
    else:
        print(b)



