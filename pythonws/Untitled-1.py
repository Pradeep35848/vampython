from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1200x600+0+0")

#=================================Variable=====================================================
        
        # self.member_var=StringVar()
        # self.prn_var=StringVar()
        # self.id_var=StringVar()
        # self.firstname_var=StringVar()
        # self.lastname_var=StringVar()
        # self.mobile_var=StringVar()
        # self.bookid_var=StringVar()
        # self.dateborrowed_var=StringVar()
        # self.datedue_var=StringVar()
        # self.daysonbook_var=StringVar()
        # self.latereturnfine_var=StringVar()

        

      
        # lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="green",fg="white",bd=10,relief=RIDGE,font=("times new roman ",40,"bold"),padx=2,pady=6)
        # lbltitle.pack(side=TOP,fill=X)

        # frame=Frame(self.root,bd=10,relief=RIDGE,padx=15,bg="green")
        # frame.place(x=0,y=100,width=1400,height=300)

        # #==================DataFrameLeft=======================================================
        # DataFrameLeft=LabelFrame(Frame,text="Library Membership Information",bg="green",bd=8,relief=RIDGE,font=("times new roman ",15,"bold"))
        # DataFrameLeft.place(x=0,y=5,width=700,height=250)
        #textvariable=self.member_var

        # lblMemebr=Label(DataFrameLeft,bg="green",text="Member Type",font=("times new roman ",15,"bold",),padx=2,pady=6)
        # lblMemebr.grid(row=0,column=0,sticky=W)

        # comMember = ttk.Combobox(DataFrameLeft,font=("times new roman ",15,"bold",),width=27,state="readonly")
        # comMember["value"]=("Admin Staf","Student","Lecturer")
        # comMember.grid(row=0,column=1)

        # lblPRN=Label(DataFrameLeft,bg="green",text="PRN No",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblPRN.grid(row=1,column=0,sticky=W)
        # txtPRN=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)#textvariable=self.prn_var,
        # txtPRN.grid(row=1,column=1)
        # lblTitle=Label(DataFrameLeft,bg="green",text="ID No:",font=("times new roman ",12,"bold"),padx=2,pady=4)
        # lblTitle.grid(row=2,column=0,sticky=W)
        # txtTitle=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)#textvariable=self.id_var,
        # txtTitle.grid(row=2,column=1)

        # lblFirstName=Label(DataFrameLeft,bg="green",text="FirstName",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblFirstName.grid(row=3,column=0,sticky=W)
        # txtFirstName=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)#textvariable=self.firstname_var
        # txtFirstName.grid(row=3,column=1)

        

        # lblLastName=Label(DataFrameLeft,bg="green",text="LastName",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblLastName.grid(row=4,column=0,sticky=W)
        # txtLastName=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)#textvariable=self.lastname_var,
        # txtLastName.grid(row=4,column=1)----------------------=================================

        # lblAddress1=Label(DataFrameLeft,bg="green",text="Address1",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblAddress1.grid(row=5,column=0,sticky=W)
        # txtAddress1=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),textvariable=self.address1_var,width=29)
        # txtAddress1.grid(row=5,column=1)

        # lblAddress2=Label(DataFrameLeft,bg="green",text="Address2",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblAddress2.grid(row=6,column=0,sticky=W)
        # txtAddress2=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),textvariable=self.address2_var,width=29)
        # txtAddress2.grid(row=6,column=1)

        # lblPostCode=Label(DataFrameLeft,bg="green",text="Post Code",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblPostCode.grid(row=7,column=0,sticky=W)
        # txtPostCode=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),textvariable=self.postcode_varwidth=29)
        # txtPostCode.grid(row=7,column=1)
#=========================================================

        # lblMobile=Label(DataFrameLeft,bg="green",text="Mobile",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblMobile.grid(row=5,column=0,sticky=W)
        # txtMobile=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)#textvariable=self.mobile_var,
        # txtMobile.grid(row=5,column=1)

        # lblBookId=Label(DataFrameLeft,bg="green",text="Book Id",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblBookId.grid(row=1,column=2,sticky=W)
        # txtBookId=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)#textvariable=self.bookid_var,
        # txtBookId.grid(row=1,column=3)=====================================================

        # lblBookTitle=Label(DataFrameLeft,bg="green",text="Book Title:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblBookTitle.grid(row=1,column=2,sticky=W)
        # txtBookTitle=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        # txtBookTitle.grid(row=1,column=3)

        # lblAuther=Label(DataFrameLeft,bg="green",text="Auther Name:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblAuther.grid(row=2,column=2,sticky=W)
        # txtAuther=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        # txtAuther.grid(row=2,column=3)
#==================================================================
        # lblDateBorrowed=Label(DataFrameLeft,bg="green",text="Date Borrowed:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblDateBorrowed.grid(row=2,column=2,sticky=W)
        # txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)#textvariable=self.dateborrowed_var,
        # txtDateBorrowed.grid(row=2,column=3)

        # lblDateDue=Label(DataFrameLeft,bg="green",text="Date Due:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblDateDue.grid(row=3,column=2,sticky=W)
        # txtDateDue=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)#textvariable=self.datedue_var,
        # txtDateDue.grid(row=3,column=3)

        # lblDaysOnBook=Label(DataFrameLeft,bg="green",text="Days On Book:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblDaysOnBook.grid(row=4,column=2,sticky=W)
        # txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)#textvariable=self.daysonbook_var,
        # txtDaysOnBook.grid(row=4,column=3)

        # lblLastReturnFine=Label(DataFrameLeft,bg="green",text="Late Return Fine:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblLastReturnFine.grid(row=5,column=2,sticky=W)
        # txtLastReturnFine=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)#textvariable=self.latereturnfine_var,
        # txtLastReturnFine.grid(row=5,column=3)==================================================================

        # lblDateOverdate=Label(DataFrameLeft,bg="green",text="Date Over date:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblDateOverdate.grid(row=7,column=2,sticky=W)
        # txtDateOverdate=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        # txtDateOverdate.grid(row=7,column=3)

        # lblActualPrice=Label(DataFrameLeft,bg="green",text="Actual Price:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        # lblActualPrice.grid(row=8,column=2,sticky=W)
        # txtActualPrice=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        # txtActualPrice.grid(row=8,column=3)
       
       #==========================Data Frame Right=================================
#=================================================
        # DataFrameRight=LabelFrame(frame,bd=8,padx=20,relief=RIDGE,bg="green",
        #                          font=("arial",15,"bold"),text ="Book Details")
        # DataFrameRight.place(x=710,y=5,width=400,height=250)

        # self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        # self.txtBox.grid(row=0,column=2)

        # listScrollbar=Scrollbar(DataFrameRight)
        # listScrollbar.grid(row=0,column=1,sticky="ns")

        # listBooks=['Python','C++','C','Java','Html','Mathe']=================================

        # def SelectBook(Event=""):
        #     value=str(listBox.get(listBox.curselection))
        #     x=value
        #     if(x=="Python"):
        #         self.bookid_var.set("BKID5454")
        #         #self.booktitle_var.set("Python Manual")
        #         #self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook.set(15)
        #         self.latereturnfine_var("Rs.10")
        #         #self.dateoverdue.set("NO")
        #         self.finallprice.set("Rs.55")

        #     elif(x=="C++"):
        #         self.bookid_var.set("BKID5454")
        #         #self.booktitle_var.set("Python Manual")
        #         #self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook.set(15)
        #         self.latereturnfine_var("Rs.5")
        #         #self.dateoverdue.set("NO")
        #         self.finallprice.set("Rs.50")

        #     elif(x=="C"):
        #         self.bookid_var.set("BKID5454")
        #         #self.booktitle_var.set("Python Manual")
        #         #self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook.set(15)
        #         self.latereturnfine_var("Rs.15")
        #         #self.dateoverdue.set("NO")
        #         self.finallprice.set("Rs.40")

        #     elif(x=="Java"):
        #         self.bookid_var.set("BKID5454")
        #         #self.booktitle_var.set("Python Manual")
        #         #self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook.set(15)
        #         self.latereturnfine_var("Rs.7")
        #         #self.dateoverdue.set("NO")
        #         self.finallprice.set("Rs.45")

        #     elif(x=="Html"):
        #         self.bookid_var.set("BKID5454")
        #         #self.booktitle_var.set("Python Manual")
        #         #self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook.set(15)
        #         self.latereturnfine_var("Rs.20")
        #         #self.dateoverdue.set("NO")
        #         self.finallprice.set("Rs.35")

        #     elif(x=="Mathe"):
        #         self.bookid_var.set("BKID5454")
        #         #self.booktitle_var.set("Python Manual")
        #         #self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook.set(15)
        #         self.latereturnfine_var("Rs.8")
        #         #self.dateoverdue.set("NO")
        #         self.finallprice.set("Rs.30")




        # listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        # listBox.bind("<<ListboxSelect>>",SelectBook)
        # listBox.grid(row=0,column=0,padx=4)
        # listScrollbar.config(command=listBox.yview)
         
        # for item in listBooks:
        #     listBox.insert(END,item)

        

        #==============================buttons Frame=========================================
        #=====================================================
        # framebutton=Frame(self.root,bd=10,relief=RIDGE,padx=15,bg="green")
        # framebutton.place(x=0,y=400,width=1400,height=40)

        # btnAddData=Button(framebutton,command=self.showData,text="Add Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        # btnAddData.grid(row=0,column=0)

        # btnAddData=Button(framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        # btnAddData.grid(row=0,column=1)

        # btnAddData=Button(framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        # btnAddData.grid(row=0,column=2)

        # btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        # btnAddData.grid(row=0,column=3)

        # btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        # btnAddData.grid(row=0,column=4)

        # btnAddData=Button(framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        # btnAddData.grid(row=0,column=5)==================================================

        #==========================Information Frame=========================================
        #==========================================
        # FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=15,bg="green")
        # FrameDetails.place(x=0,y=401,width=1520,height=159)===========================
        
        # Table_frame=Frame(FrameDetails,bd=5,relief=RIDGE,bg="green")
        # Table_frame.place(x=0,y=2,width=1310,height=110)

        # xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        # yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        # self.libary_table=ttk.Treeview(Table_frame,column=("memebertype","prnno","id","firtname",
        #                                                    "lastname","mobile","bookid","dateborrowed",
        #                                                    "datedue","days","latereturnFine"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        # xscroll.pack(side=BOTTOM,fill=X)
        # yscroll.pack(side=RIGHT,fill=Y)

        # xscroll.config(command=self.libary_table.xview)
        # yscroll.config(command=self.libary_table.yview)
        

        # self.libary_table.heading("memebertype",text="Member Type")
        # self.libary_table.heading("prnno",text="PRN No")
        # self.libary_table.heading("id",text="ID")
        # self.libary_table.heading("fristname",text="Frist Name")
        # self.libary_table.heading("lastname",text="Last Name")
        # self.libary_table.heading("mobile",text="Mobile Number")
        # self.libary_table.heading("bookid",text="Book ID")
        # self.libary_table.heading("dateborrowed",text="Date of Borrowed")
        # self.libary_table.heading("datedue",text="Date Due")
        # self.libary_table.heading("days",text="DaysOnBook")
        # self.libary_table.heading("latereturnfine",text="LateReturnFine")
        
        # self.libary_table["show"]="headings"
        # self.libary_table.pack(fill=BOTH,expand=1)

        # self.libary_table.column("membertype",width=100)
        # self.libary_table.column("prnno",width=100)
        # self.libary_table.column("id",width=100)
        # self.libary_table.column("fristname",width=100)
        # self.libary_table.column("lastname",width=100)
        # self.libary_table.column("mobile",width=100)
        # self.libary_table.column("bookid",width=100)
        # self.libary_table.column("dateborrowed",width=100)
        # self.libary_table.column("datedue",width=100)
        # self.libary_table.column("days",width=100)
        # self.libary_table.column("latereturnfine",width=100)

        # self.fatch_data()
        # self.libary_table.bind("<ButtonRelease-1>",self.get_cursor)

    # def adda_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
    #                                                                                     self.member_var.get(),
    #                                                                                     self.prn_par.get(),
    #                                                                                     self.id_var.get(),
    #                                                                                     self.firstname_var.get(),
    #                                                                                     self.lastname_var.get(),
    #                                                                                     self.member_var.get(),
    #                                                                                     self.bookid_var.get(),
    #                                                                                     self.dateborrowed_var.get(),
    #                                                                                     self.datedue_var.get(),
    #                                                                                     self.daysonbook.get(),
    #                                                                                     self.latereturnfine_var.get(),
                                                                                        
    #                                                                                     ))
        
    #     conn.commit()
    #     self.fatch_data()
    #     conn.close()
           
    #     messagebox.showinfo("success","Member Has been inserted successfully")



    # def update(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Member=%s,BookID=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,PRN=%s",(
    #                                                                                     self.member_var.get(),
                                                                                       
    #                                                                                     self.id_var.get(),
    #                                                                                     self.firstname_var.get(),
    #                                                                                     self.lastname_var.get(),
    #                                                                                     self.member_var.get(),
    #                                                                                     self.bookid_var.get(),
    #                                                                                     self.dateborrowed_var.get(),
    #                                                                                     self.datedue_var.get(),
    #                                                                                     self.daysonbook.get(),
    #                                                                                     self.latereturnfine_var.get(),
    #                                                                                     self.prn_par.get(),
    #                                                                                     ))
        

    #     conn.commit()
    #     self.fatch_data()
    #     conn.close()
           
    #     messagebox.showinfo("success","Member Has been updated ")


    # def fatch_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("select*from library")
    #     rows=my_cursor.fetchall()

    #     if len(rows)!=0:
    #          self.libary_table.delete(*self.libary_table.get_children())
    #          for i in rows:
    #             self.libary_table.insert("",END,values=i)
    #     conn.commit()
    #     conn.close()

    # def get_cursor(self,event=""):
    #     cursor_row=self.libary_table.focus()
    #     content=self.libary_table.item(cursor_row)
    #     row=content['values']

    #     self.member_var.set(row[0]) 
    #     self.prn_var.set(row[1])
    #     self.id_var.set(row[2])
    #     self.firstname_var.set(row[3])
    #     self.lastname_var.set(row[4])
    #     self.mobile_var.set(row[5])
    #     self.bookid_var.set(row[6])
    #     self.dateborrowed_var.set(row[7])
    #     self.datedue_var.set(row[8])
    #     self.daysonbook_var.set(row[9]) 
    #     self.latereturnfine_var.set(row[10]) 
    
    # def showData(self):
    #     self.txtBox.insert(END,"Member Type\t\t" + self.member_var.get()+"\n")
    #     self.txtBox.insert(END,"PRN NO:\t\t" + self.prn_var.get()+"\n")
    #     self.txtBox.insert(END,"ID NO:\t\t" + self.id_var.get()+"\n")
    #     self.txtBox.insert(END,"FirstName\t\t" + self.firstname_var.get()+"\n")
    #     self.txtBox.insert(END,"LastName\t\t" + self.lastname_var.get()+"\n")
    #     self.txtBox.insert(END,"MObile NO:\t\t" + self.mobile_var.get()+"\n")
    #     self.txtBox.insert(END,"Book ID:\t\t" + self.bookid_var.get()+"\n")
    #     self.txtBox.insert(END,"DateBorrowed\t\t" + self.dateborrowed_var.get()+"\n")
    #     self.txtBox.insert(END,"DateDue\t\t" + self.datedue_var.get()+"\n")
    #     self.txtBox.insert(END,"DaysOnBook\t\t" + self.daysonbook.get()+"\n")
    #     self.txtBox.insert(END,"LateReturnFine\t\t" + self.latereturnfine_var.get()+"\n")

    # def reset(self):
    #     self.member_var.set(""),
    #     self.prn_var.set(""),
    #     self.id_var.set(""),
    #     self.firstname_var.set(""),
    #     self.lastname_var.set(""),
    #     self.mobile_var.set(""),
    #     self.bookid_var.set(""),
    #     self.dateborrowed_var.set(""),
    #     self.datedue_var.set(""),
    #     self.daysonbook.set(""),
    #     self.latereturnfine_var.set("")
    #     self.txtBox.delete("1.0",END)

    # def iExit(self):
    #     iExit=tkinter.messagebox.askyesno("Library mangement System","Doyou want to exit")
    #     if iExit>0:
    #         self.root.destroy()
    #         return

               
    # def delete(self):
    #     if self.prn_var.get()==""or self.id_var.get()=="":
    #         messagebox.showerror("Error","First Selct the Member")
    #     else:
    #         conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    #         my_cursor=conn.cursor()
    #         query="delete from library where PRN_NO=%s"
    #         value=(self.prn_var.get(),)
    #         my_cursor.execute(query,value)

    #         conn.commit()
    #         self.fatch_data()
    #         self.reset()
    #         conn.close()

    #         messagebox.showinfo("Success","Member has been Deleted")

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()


    
