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

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="green",fg="white",bd=10,relief=RIDGE,font=("times new roman ",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=0,relief=RIDGE,padx=18,bg="green")
        frame.place(x=0,y=100,width=1430,height=350)


#==================DataFrameLeft=======================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="green",bd=10,relief=RIDGE,font=("times new roman ",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=760,height=300)


#==========================Data Frame Right=================================

        DataFrameRight=LabelFrame(frame,bd=10,padx=18,relief=RIDGE,bg="green",
                                 font=("arial",10,"bold"),text ="Book Details")
        DataFrameRight.place(x=750,y=5,width=480,height=300)

#==============================buttons Frame=========================================
        framebutton=Frame(self.root,bd=10,relief=RIDGE,padx=18,bg="green")
        framebutton.place(x=0,y=400,width=1430,height=70)



#==========================Information Frame=========================================
        FrameDetails=Frame(self.root,bd=10,relief=RIDGE,padx=18,bg="green")
        FrameDetails.place(x=0,y=500,width=1430,height=195)



if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
