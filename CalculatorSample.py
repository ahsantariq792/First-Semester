from tkinter import*
from math import*
m=Tk()
m.title("Calculator")
def b1():
    a1.insert(0,1)
def add():
    x=a1.get()
    y=a2.get()
    z=int(x)+int(y)
    a3.delete(0,z)
    a3.insert(4,z)
def subtract():
    x=a1.get()
    y=a2.get()
    z=int(x)-int(y)
    a3.delete(0, z)
    a3.insert(4, z)
def multiply():
    x=a1.get()
    y=a2.get()
    z=int(x)*int(y)
    a3.delete(0,z)
    a3.insert(4,z)
def divide():
    x=a1.get()
    y=a2.get()
    z=int(x)//int(y)
    a3.delete(0,z)
    a3.insert(4,z)
def sin():
    x=int(a1.get())
    z=sin(x)
    a3.delete(0, 1)
    a3.insert(0, z)
def cos():
    x=a1.get()
    z=cos(x)
    a3.delete(0, 1)
    a3.insert(4, z)
def tan():
    x=a1.get()
    z=tan(x)
    a3.delete(0, 1)
    a3.insert(4, z)
def squart():
    x=int(a1.get())
    z=sqrt(x)
    a3.delete(0,z)
    a3.insert(4,z)
def pow2():
    x=int(a1.get())
    z=x**2
def pow3():
    x=int(a1.get())
    z=x**3

def Asin():
    x=int(a1.get())
    z=asin(x)
def fact():
    n=a1.get()
    num=int(n)
    if num==0 or num==1:
        z=0
    elif num>1:
        for i in range(1,num):
            num=num*i
            z=int(num)
        a3.delete(0,z)
        a3.insert(4,z)


a1=Entry(m,width=30)
a1.grid(row=1,column=2,pady=10)
a2=Entry(m,width=30)
a2.grid(row=2,column=2,pady=10)
a3=Entry(m,width=30)
a3.grid(row=4,column=4)
A=Button(m,text="+",bg='light blue',command=add,fg='black',bd=5,pady=10)
A.grid(row=4,column=0)
S=Button(m,text="-",bg='light blue',command=subtract,fg='black',bd=5,pady=10)
S.grid(row=4,column=1)
M=Button(m,text="x",bg='light blue',command=multiply,fg='black',bd=5,pady=10)
M.grid(row=5,column=0)
D=Button(m,text="/",bg='light blue',fg='black',command=divide,bd=5,pady=10)
D.grid(row=5,column=1)
l1=Label(m,text="Answer=").grid(row=4,column=3)
s1=Button(m,text="Sin",bg='pink',fg='black',command=sin,pady=10).grid(row=6,column=0)
s2=Button(m,text="Cos",bg='pink',fg='black',command=cos,pady=10).grid(row=6,column=1)
s3=Button(m,text="Tan",bg='pink',fg='black',command=tan,pady=10).grid(row=7,column=0)
s4=Button(m,text="√",bg='pink',fg='black',command=squart,pady=10).grid(row=7,column=1)
s5=Button(m,text="n!",bg='pink',fg='black',command=fact,pady=10).grid(row=8,column=0)
r1=Button(m,text="1",bg='pink',fg='black',command=b1,pady=10).grid(row=4,column=2)
m.mainloop()