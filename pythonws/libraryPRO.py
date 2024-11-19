from tkinter import*

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1200x600+0+0")

      
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="green",fg="white",bd=10,relief=RIDGE,font=("times new roman ",40,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=10,relief=RIDGE,padx=15,bg="green")
        frame.place(x=0,y=100,width=1400,height=300)

        #==================DataFrameLeft=======================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="green",bd=8,relief=RIDGE,font=("times new roman ",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=250)

        lblMemebr=Label(DataFrameLeft,bg="green",text="Member Type",font=("times new roman ",15,"bold",),padx=2,pady=6)
        lblMemebr.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,font=("times new roman ",15,"bold",),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="green",text="PRN No",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="green",text="ID No:",font=("times new roman ",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="green",text="FirstName",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        

        lblLastName=Label(DataFrameLeft,bg="green",text="LastName",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="green",text="Address1",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="green",text="Address2",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="green",text="Post Code",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)


        lblMobile=Label(DataFrameLeft,bg="green",text="Mobile",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman ",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="green",text="Book Id",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="green",text="Book Title:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="green",text="Auther Name:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="green",text="Date Borrowed:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="green",text="Date Due:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="green",text="Days On Book:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLastReturnFine=Label(DataFrameLeft,bg="green",text="Last Return Fine:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblLastReturnFine.grid(row=6,column=2,sticky=W)
        txtLastReturnFine=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtLastReturnFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameLeft,bg="green",text="Date Over date:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtDateOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="green",text="Actual Price:",font=("times new roman ",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman ",12,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)
       
       #==========================Data Frame Right=================================

        DataFrameRight=LabelFrame(frame,bd=8,padx=20,relief=RIDGE,bg="green",
                                 font=("arial",15,"bold"),text ="Book Details")
        DataFrameRight.place(x=710,y=5,width=400,height=250)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Python','C++','C','Java','Html','Mathe']



        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
         
        for item in listBooks:
            listBox.insert(END,item)

        

        #==============================buttons Frame=========================================
        framebutton=Frame(self.root,bd=10,relief=RIDGE,padx=15,bg="green")
        framebutton.place(x=0,y=400,width=1400,height=40)

        btnAddData=Button(framebutton,text="Add Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=5)

        #==========================Information Frame=========================================
        frameDetails=Frame(self.root,bd=10,relief=RIDGE,padx=15,bg="green")
        frameDetails.place(x=0,y=400,width=1400,height=150)
        
        Table_frame=frame(frameDetails,bd=5,relief=RIDGE,bg="green")
        Table_frame.place(x=0,y=2,width=1310,height=110)

        xscroll=ttk.Srollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Srollbar(Table_frame,orient=VERTICAL)

        self.libary_table=ttk.Treeview(Table_frame,column=("memebertype","prnno","firtname",
                                                           "lastname","mobile","bookid","dateborrowed",
                                                           "datedue","days"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)


if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()



    