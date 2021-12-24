import tkinter as tk
from tkinter import *
import statistics as stats
import pandas as pd
from tkinter import messagebox

root =tk.Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.title("measures of center")
root.geometry("%dx%d" % (width, height))
root.state('zoomed')
root.config(bg="#84e9d9")



df=pd.read_csv("cardio_train.csv")

lists=df.columns
opts=StringVar(root)
opts.set("select the column")
men=OptionMenu(root,opts,*lists)
men.place(x=350,y=80,width=500)

def select(men):
    data=opts.get()
    if(df[opts.get()].dtypes==object):
         tk.messagebox.showinfo(
         title='not valid data',
         message= "invalid data please select valid data"
        )  
         return
    return data
# button=Button(root,text="click to get the selection value",command=lambda:select(men))
# button.place(x=860,y=80)
data=select
def buttonmodefunc():
    c=stats.mode(df[data])
    lab1=Label(text="mode=",bg="white",fg="black",width="10",height="2")
    lab1.place(x=650,y=150)
    l1=Label(text=c,bg="white",fg="black",width="20",height="2")
    l1.place(x=720,y=150)



def buttonmedianfunc():
    c=stats.median(df[data])
    lab2=Label(text="median=",bg="white",fg="black",width="10",height="2")
    lab2.place(x=650,y=270)
    l2=Label(text=c,bg="white",fg="black",width="20",height="2")
    l2.place(x=720,y=270)



def buttonmeanfunc():
    c=stats.mean(df[data])
    lab3=Label(text="mean=",bg="white",fg="black",width="10",height="2")
    lab3.place(x=650,y=390)
    l3=Label(text=c,bg="white",fg="black",width="20",height="2")
    l3.place(x=720,y=390)
    

def buttonvariancefunc():
    c=stats.variance(df[data])
    lab1=Label(text="variance=",bg="white",fg="black",width="20",height="2")
    lab1.place(x=650,y=510)
    l1=Label(text=c,bg="white",fg="black",width="20",height="2")
    l1.place(x=750,y=510)

def buttonpvariancefunc():
    c=stats.pvariance(df[data])
    lab1=Label(text="Stand. Dev.=",bg="white",fg="black",width="20",height="2")
    lab1.place(x=650,y=630)
    l1=Label(text=c,bg="white",fg="black",width="20",height="2")
    l1.place(x=760,y=630)
  




b1=Button(root,text="press to calc mode",command=buttonmodefunc)
b1.config(font=("Helvetica",15,"bold"))
b1.place(x=360,y=150)

b2=Button(root,text="press to calc median",command=buttonmedianfunc)
b2.config(font=("Helvetica",15,"bold"))
b2.place(x=360,y=270)

b3=Button(root,text="press to calc mean",command=buttonmeanfunc)
b3.config(font=("IHelvetica",15,"bold"))
b3.place(x=360,y=390)

b4=Button(root,text="press to calc variance",command=buttonvariancefunc)
b4.config(font=("Helvetica",15,"bold"))
b4.place(x=360,y=510)

b5=Button(root,text="press to calc Stand. Dev.",command=buttonpvariancefunc)
b5.config(font=("Helvetica",15,"bold"))
b5.place(x=360,y=630)




root.mainloop()