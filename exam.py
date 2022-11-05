from tkinter import *
import tkinter as tk
from tkinter import ttk

window=Tk()
window.geometry("1500x700")
window.configure(bg="pink")
def insert():
    pass

f_name=StringVar()
l_name=StringVar()
E_mail=StringVar()
zip_code=IntVar()



lb=Listbox(window,width=50,height=22)
lb.place(x=20,y=30)


lb1=Listbox(window,width=50,height=22)
lb1.place(x=470,y=30)

b=Button(window,text="Insert" ,width=10,command=insert)
b.place(x=360,y=120)

b1=Button(window,text="Delete" ,width=10)
b1.place(x=360,y=180)

b2=Button(window,text="Theme" ,width=10)
b2.place(x=360,y=240)

l=Label(window,text="First Name:",background="white" )
l.place(x=30,y=40)

e=Entry(window,textvariable=f_name,font=('Arial',10,'normal'))
e.place(x=110,y=40)

l=Label(window,text="Last Name:",background="white")
l.place(x=30,y=70)

e1=Entry(window,textvariable=l_name,font=('Arial',10,'normal'))
e1.place(x=110,y=70)

l1=Label(window,text="Gender:",background="white")
l1.place(x=30,y=100)

r=Radiobutton(window, text='Male', value='Value 1',background='white')
r.place(x=110,y=100)

r1=Radiobutton(window, text='Female', value='Value 2',background='white')
r1.place(x=170,y=100)


l2=Label(window,text="Languages:",background="white")
l2.place(x=30,y=130)

c=Checkbutton(window,text='Telugu',background='white')
c.place(x=110,y=130)

c1=Checkbutton(window,text='English',background='white')
c1.place(x=180,y=130)

c2=Checkbutton(window,text='Hindi',background='white')
c2.place(x=250,y=130)

l3=Label(window,text="Email:",background="white")
l3.place(x=30,y=160)

e2=Entry(window,textvariable=E_mail,background='white')
e2.place(x=110,y=160)

l4=Label(window,text="Adress:",background="white")
l4.place(x=30,y=190)

lb2=Listbox(window,width=25,height=5)
lb2.place(x=110,y=190)


window.mainloop()