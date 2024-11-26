# import mysql.connector as a
# con=a.connect(host="localhost",user="root",passsword="12345",database="library")

# def addbook():
#     bn=input("Enter Book Name:")
#     c=input("Enter Book Code:")
#     t=input("Total Books:")
#     s=input("Enter Subject:")
#     data=(bn,c,t,s)
#     sql='insert into books values(%s,%s,%s,%s)'
#     c=con.cursor()
#     c.execute(sql,data)
#     con.commit()
#     print(">--------------------------------------------------------------------------------------------------------<")
#     print("Data Entered Successfully")
#     main()

#     def issueb():
#         n=input("Enter Name:")
#         r=input("Enter Reg No:")
#         co=input("Enter Book Code:")
#         d=input("Enter Date:")
#         a="insert into issue values(%s,%s,%s,%s)"
#         data=(n,r,co,d)
#         c=con.cursor()
#         c.execute(a,data)
#         con.commit()
#         print(">-----------------------------------------------------------------------<")
#         print("Book issued to:",n)
#         bookup(co,-1)

#     def submitd():
#         n=input("Enter Name:")
#         r=input("Enter Reg No:")
#         co=input("Enter Book Code:")
#         d=input("Enter Date:")
#         a="insert into submit values(%s,%s,%s,%s)"
#         data=(n,r,co,d)
#         c=con.cursor()
#         c.execute(a,data)
#         con.commit()
#         print(">-----------------------------------------------------------------------<")
#         print("Book Submitted from:",n)
#         bookup(co,1)

#     def bookup(co,u):
#         a="select TOTAL from books where BCODE=%s"
#         data=(co,)
#         c=con.cursor()
#         c.execute(a,data)
#         myresult=c.fetchone()
#         t=myresult[0]+u
#         sql="update books set TOTAL =%s where BCODE=%s"
#         d=(t,co)
#         c.execute(sql,d)
#         con.commit()
#     main()

#     def dbook():
#             ac=input("Enter Book Code:")
#             a="delete frpm books where BCODE =%s"
#             data=(co,)
#             c=con.cursor()
#             c.execute(a,data)
#             con.commit()
#     main()


#     def  dispbook():
#          a="select from books"
#          c=con.cursor()
#          c.execute(a)
#          myresult=c.fetchall()
#          for i in myresult:
#               print("Book Name:",i[0])
#               print("Book Code:",i[1])
#               print("Total:",i[2])
#               print(">----------------------------------<")
#     main()

    

#     def main():
#          print("""
#                                             LIBRARY MANAGER
#                1.ADD BOOK
#                2.ISSUE BOOK 
#                3.SUBMIT BOOK 
#                4.DELETE BOOK 
#                5.DISPLAY BOOKS 
#                """)
#          choice=input("Enter Task No:")
#          print(">----------------------------------------------------<")
#          if(choice=='1'):
#             addbook()
#          elif(choice=='2'):
#               issueb()
#          elif(choice=='3'):
#               submitd()
#          elif(choice=='4'):
#               dbook()
#          elif(choice=='5'):
#               dispbook()
#          else:
#               print("Wrong choice...................")
#               main()
    
#     def pswd():
#          ps=input("Enter Password:")
#          if ps=="py143":
#               main()
#          else:
#               print("Wrong Password")
#               pswd()
#               pswd()


import mysql.connector as a

con = a.connect(host="localhost", user="root", password="12345", database="library")

def addbook():
    bn = input("Enter Book Name: ")
    c = input("Enter Book Code: ")
    t = input("Total Books: ")
    s = input("Enter Subject: ")
    data = (bn, c, t, s)
    sql = 'INSERT INTO books VALUES (%s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print(">--------------------------------------------------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueb():
    n = input("Enter Name: ")
    r = input("Enter Reg No: ")
    co = input("Enter Book Code: ")
    d = input("Enter Date: ")
    a = "INSERT INTO issue VALUES (%s, %s, %s, %s)"
    data = (n, r, co, d)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    print(">-----------------------------------------------------------------------<")
    print("Book issued to:", n)
    bookup(co, -1)

def submitd():
    n = input("Enter Name: ")
    r = input("Enter Reg No: ")
    co = input("Enter Book Code: ")
    d = input("Enter Date: ")
    a = "INSERT INTO submit VALUES (%s, %s, %s, %s)"
    data = (n, r, co, d)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    print(">-----------------------------------------------------------------------<")
    print("Book Submitted from:", n)
    bookup(co, 1)

def bookup(co, u):
    a = "SELECT TOTAL FROM books WHERE BCODE = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "UPDATE books SET TOTAL = %s WHERE BCODE = %s"
    d = (t, co)
    c.execute(sql, d)
    con.commit()

def dbook():
    ac = input("Enter Book Code: ")
    a = "DELETE FROM books WHERE BCODE = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a, data)
    con.commit()

def dispbook():
    a = "SELECT * FROM books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name:", i[0])
        print("Book Code:", i[1])
        print("Total:", i[2])
        print(">----------------------------------<")

def main():
    print("""
                                    LIBRARY MANAGER
               1.ADD BOOK
               2.ISSUE BOOK
               3.SUBMIT BOOK
               4.DELETE BOOK
               5.DISPLAY BOOKS
               """)
    choice = input("Enter Task No: ")
    print(">----------------------------------------------------<")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        submitd()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        dispbook()
    else:
        print("Wrong choice...................")
        main()

def pswd():
    ps = input("Enter Password: ")
    if ps == "py143":
        main()
    else:
        print("Wrong Password")
        pswd()

# Start the program by asking for the password
pswd()
