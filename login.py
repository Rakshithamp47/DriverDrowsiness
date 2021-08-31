import tkinter
from tkinter import*
from tkinter import messagebox
import os
top=tkinter.Tk(className="LOGIN")
name="rvce"
pas="rvce"

user=StringVar()
pwd=StringVar()

def login():
	if(user.get()==name and pwd.get()==pas):
		messagebox.showinfo("alert","login Done")
	else:
		messagebox.showinfo("alert","Wrong passwd or user name")
def callback():
	os.system('python3 driverdrowsy.py')
	
l1=Label(top,text="USER NAME")
user=Entry(top,textvariable=user)
l2=Label(top,text="PASSWORD")
pwd=Entry(top,textvariable=pwd,show="*")
b1=Button(top,text="SUBMIT",command=callback)
b2=Button(top,text="CLEAR",command=callback)

l1.pack()
user.pack()
l2.pack()
pwd.pack()
b1.pack()
b2.pack()

top.mainloop()
