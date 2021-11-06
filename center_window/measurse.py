import tkinter as tk
from tkinter import *
import numpy as np
import statistics as stats
from statistics import *
import pandas as pd

df=pd.read_csv("center_window/dataframe.csv")

def buttonmodefunc():
    c=stats.mode(df["data"])
    lab1=Label(text="mode=",bg="white",fg="black",width="10",height="2")
    lab1.place(x=600,y=30)
    l1=Label(text=c,bg="white",fg="black",width="100",height="2")
    l1.place(x=670,y=30)


def buttonmedianfunc():
    c=stats.median(df["data"])
    lab2=Label(text="median=",bg="white",fg="black",width="10",height="2")
    lab2.place(x=600,y=180)
    l2=Label(text=c,bg="white",fg="black",width="100",height="2")
    l2.place(x=670,y=180)


def buttonmeanfunc():
    c=stats.mean(df["data"])
    lab3=Label(text="mean=",bg="white",fg="black",width="10",height="2")
    lab3.place(x=600,y=330)
    l3=Label(text=c,bg="white",fg="black",width="100",height="2")
    l3.place(x=670,y=330)

def buttonvariancefunc():
    c=stats.variance(df["data"])
    lab1=Label(text="Standard Deviation=",bg="white",fg="black",width="20",height="2")
    lab1.place(x=600,y=480)
    l1=Label(text=c,bg="white",fg="black",width="100",height="2")
    l1.place(x=740,y=480)

def buttonpvariancefunc():
    c=stats.pvariance(df["data"])
    lab1=Label(text="variance=",bg="white",fg="black",width="10",height="2")
    lab1.place(x=600,y=630)
    l1=Label(text=c,bg="white",fg="black",width="100",height="2")
    l1.place(x=670,y=630)    


root =tk.Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.title("measures of center")
root.geometry("%dx%d" % (width, height))
root.state('zoomed')
root.config(bg="#84e9d9")

b1=Button(root,text="press to calc mode",command=buttonmodefunc)
b1.config(font=("Helvetica",15,"bold"))
b1.place(x=150,y=30)

b2=Button(root,text="press to calc median",command=buttonmedianfunc)
b2.config(font=("Helvetica",15,"bold"))
b2.place(x=150,y=180)

b3=Button(root,text="press to calc mean",command=buttonmeanfunc)
b3.config(font=("IHelvetica",15,"bold"))
b3.place(x=150,y=330)

b4=Button(root,text="press to calc variance",command=buttonvariancefunc)
b4.config(font=("Helvetica",15,"bold"))
b4.place(x=150,y=480)

b5=Button(root,text="press to calc Standard Deviation",command=buttonpvariancefunc)
b5.config(font=("Helvetica",15,"bold"))
b5.place(x=150,y=630)

root.mainloop()