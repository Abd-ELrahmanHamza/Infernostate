import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import statistics as stats
from statistics import *
import pandas as pd
from tkinter  import messagebox,Tk

class title:
    def __init__(self, root, font):
        topFrame = tk.Frame(root)
        topFrame.pack(side=tk.TOP, pady=20)
        label = tk.Label(topFrame, text="Measure Of Center", font=font + (40, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack()

def run(dataFrame):
    root = tk.Tk()
    root.title("Infernostate")
    root.config(bg="#84e9d9")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.state('zoomed')
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.title("measures of center")
    font = ("Helvetica",)
    root.option_add('*TCombobox*Listbox.font', font+(15,)) # apply font to combobox
    root.config(bg="#84e9d9")
    # title(root,font)
    # your code here
    

    # print(dataFrame)
    df=dataFrame
    lists=df.columns
    
    frameOptions = tk.Frame(root, bg="#84e9d9")
    frameOptions.pack(pady=10)
    opts=StringVar(root)
    opts.set("Select the Column")
    lists = lists.tolist()
    men=ttk.Combobox(root,width=30, justify='center', height=len(lists),textvariable=opts,values=lists ,font=font+(16,))
    men.place(x=350,y=80,width=500)
    men.option_add('*TCombobox*Listbox.Justify', 'center')



    def select(men):
        data=opts.get()
        if(df[opts.get()].dtypes==object):
           tk.messagebox.showinfo(
           title='not valid data',
           message= "invalid data please select valid data"
           )  
           return
        return data
    data=select
    def buttonmodefunc():
        c=stats.mode(df[data])
        lab1=Label(root,text="mode=",bg="white",fg="black",width="10",height="2")
        lab1.place(x=650,y=150)
        l1=Label(root,text=c,bg="white",fg="black",width="20",height="2")
        l1.place(x=720,y=150)


    def buttonmedianfunc():
        c=stats.median(df[data])
        lab2=Label(root,text="median=",bg="white",fg="black",width="10",height="2")
        lab2.place(x=650,y=270)
        l2=Label(root,text=c,bg="white",fg="black",width="20",height="2")
        l2.place(x=720,y=270)


    def buttonmeanfunc():
        c=stats.mean(df[data])
        lab3=Label(root,text="mean=",bg="white",fg="black",width="10",height="2")
        lab3.place(x=650,y=390)
        l3=Label(root,text=c,bg="white",fg="black",width="20",height="2")
        l3.place(x=720,y=390)

    def buttonvariancefunc():
        c=stats.variance(df[data])
        lab4=Label(root,text="variance=",bg="white",fg="black",width="20",height="2")
        lab4.place(x=650,y=510)
        l4=Label(root,text=c,bg="white",fg="black",width="20",height="2")
        l4.place(x=750,y=510)

    def buttonpvariancefunc():
        c=stats.pvariance(df[data])
        lab5=Label(root,text="Stand. Dev.=",bg="white",fg="black",width="20",height="2")
        lab5.place(x=650,y=630)
        l5=Label(root,text=c,bg="white",fg="black",width="20",height="2")
        l5.place(x=760,y=630)    


    # frameBtns1 = tk.Frame(root, bg="#84e9d9")
    # frameBtns1.pack(pady=0)
    # button = tk.Button(frameBtns1, text='press to calc mode', command=buttonmodefunc, font=font + (20,), bg="#4b50b0",fg="#efefef",width = 10)
    # button.pack(side=tk.LEFT,padx = 10,pady = 300)
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
