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
        topFrame.pack(side=tk.TOP,pady=20)
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
    root.title("Measure Of Center")
    font = ("Helvetica",)
    root.option_add('*TCombobox*Listbox.font', font+(15,)) # apply font to combobox
    root.config(bg="#84e9d9")
    title(root,font)
    # your code here
    

    df=dataFrame
    lists=df.columns
    
    frameOptions = tk.Frame(root, bg="#84e9d9")
    frameOptions.pack(side=tk.TOP,pady=40)
    opts=StringVar(root)
    opts.set("Select the Column")
    lists = lists.tolist()
    men=ttk.Combobox(frameOptions,width=30, justify='center', height=len(lists),textvariable=opts,values=lists ,font=font+(16,))
    men.option_add('*TCombobox*Listbox.Justify', 'center')
    men.pack()


    def select(men):
        data=opts.get()
        if(df[opts.get()].dtypes==object):
            messagebox.showinfo(
            title='Error!',
            message= "Invalid data please select valid data"
            )  
            return
        return data
    data=select
    def buttonmodefunc():
        if(opts.get() == 'Select the Column'):
            l1.config(text = 'Select a Column')
        else:
            c=stats.mode(df[data])
            l1.config(text = c)
    
        
    def buttonmedianfunc():
        if(opts.get() == 'Select the Column'):
            l2.config(text = 'Select a Column')
        else:
            c=stats.median(df[data])
            l2.config(text = c)

    def buttonmeanfunc():
        if(opts.get() == 'Select the Column'):
            l3.config(text = 'Select a Column')
        else:
            c=stats.mean(df[data])
            l3.config(text = c)

    def buttonvariancefunc():
        if(opts.get() == 'Select the Column'):
            l4.config(text = 'Select a Column')
        else:
            c=stats.variance(df[data])
            l4.config(text = c)

    def buttonpvariancefunc():
        if(opts.get() == 'Select the Column'):
            l5.config(text = 'Select a Column')
        else:
            c=stats.stdev(df[data])
            l5.config(text = c) 


    frameBtns1 = tk.Frame(root, bg="#84e9d9")
    frameBtns1.pack(pady=20)
    button1 = tk.Button(frameBtns1, text='Calculate Mode', command=buttonmodefunc, font=font + (20,), bg="#4b50b0",fg="#efefef",width = 30)
    l1=Label(frameBtns1,text='', bg="#4b50b0",fg="#efefef",width="20",font=font + (20,))
    l1.pack(side = tk.RIGHT,padx=20)
    button1.pack(side = tk.RIGHT)



    frameBtns2 = tk.Frame(root, bg="#84e9d9")
    frameBtns2.pack(pady=20)
    l2=Label(frameBtns2,text='', bg="#4b50b0",fg="#efefef",width="20",font=font + (20,))
    l2.pack(side = tk.RIGHT,padx=20)
    button2 = tk.Button(frameBtns2, text='Calculate Median', command=buttonmedianfunc, font=font + (20,), bg="#4b50b0",fg="#efefef",width = 30)
    button2.pack(side = tk.RIGHT)


    frameBtns3 = tk.Frame(root, bg="#84e9d9")
    frameBtns3.pack(pady=20)
    l3=Label(frameBtns3,text='', bg="#4b50b0",fg="#efefef",width="20",font=font + (20,))
    l3.pack(side = tk.RIGHT,padx=20)
    button3 = tk.Button(frameBtns3, text='Calculate Mean', command=buttonmeanfunc, font=font + (20,), bg="#4b50b0",fg="#efefef",width = 30)
    button3.pack(side = tk.RIGHT)



    frameBtns4 = tk.Frame(root, bg="#84e9d9")
    frameBtns4.pack(pady=20)
    l4=Label(frameBtns4,text='', bg="#4b50b0",fg="#efefef",width="20",font=font + (20,))
    l4.pack(side = tk.RIGHT,padx=20)
    button4 = tk.Button(frameBtns4, text='Calculate Variance', command=buttonvariancefunc, font=font + (20,), bg="#4b50b0",fg="#efefef",width = 30)
    button4.pack(side = tk.RIGHT)


    frameBtns5 = tk.Frame(root, bg="#84e9d9")
    frameBtns5.pack(pady=20)
    l5=Label(frameBtns5,text='', bg="#4b50b0",fg="#efefef",width="20",font=font + (20,))
    l5.pack(side = tk.RIGHT,padx=20)
    button5 = tk.Button(frameBtns5, text='Calculate Standard Deviation', command=buttonpvariancefunc, font=font + (20,), bg="#4b50b0",fg="#efefef",width = 30)
    button5.pack(side = tk.RIGHT)


    root.mainloop()
