import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
from statistics import *
from collections import Counter
import pandas as pd
from tkinter  import messagebox,Tk
options = ['Bar Char', 'Histogram', 'Dot Digram',
           'Box plot', 'Stem-and-leaf Plot','viloent']

#title of the window
class title:
    def __init__(self, root, font):
        topFrame = tk.Frame(root)
        topFrame.pack(side=tk.TOP, pady=20)
        label = tk.Label(topFrame, text="Ploting", font=font + (40, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack()

class HistogramBtn:
    def __init__(self, frame, font,dataFrame,menu1):
        self.dataFrame = dataFrame
        self.menu1=menu1
        button = tk.Button(frame, text='Histogram', command=self.plot, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10,pady = 300)

    def plot(self):
        plt.close("all")
        if(self.menu1.get()=='Select the Column'):
            tk.messagebox.showinfo(
            title='Warning',
            message="No Column selected"
            )
        else:
            plt.hist(self.dataFrame[self.menu1.get()],color = 'maroon')
            plt.get_current_fig_manager().canvas.set_window_title('Histogram')
            plt.title(self.menu1.get().capitalize())
            plt.xlabel('Values')
            plt.ylabel('Frequency')
            plt.show()
        pass


class BarGraphBtn:
    def __init__(self, frame, font,dataFrame,menu1):
        self.dataFrame = dataFrame
        self.menu1 = menu1
        button = tk.Button(frame, text='Bar Chart', command=self.plot, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10,pady = 300)

    def plot(self):
        plt.close("all")
        if(self.menu1.get()=='Select the Column'):
            tk.messagebox.showinfo(
            title='Warning',
            message="No Column selected"
            )
        else:
            plt.hist(self.dataFrame[self.menu1.get()],color = 'maroon',rwidth=0.5)
            plt.get_current_fig_manager().canvas.set_window_title('Bar Chart')
            plt.title(self.menu1.get().capitalize())
            plt.xlabel('Values')
            plt.ylabel('Frequency')
            plt.show()
        pass



class BoxPlotGraphBtn:
    def __init__(self, frame, font,dataFrame,menu1):
        self.dataFrame = dataFrame
        self.menu1 = menu1
        button = tk.Button(frame, text='Box plot', command=self.plot, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10,pady = 300)

    def plot(self):
        plt.close("all")
        if(self.menu1.get()=='Select the Column'):
            tk.messagebox.showinfo(
            title='Warning',
            message="No Column selected"
            )
        else:
            if(self.dataFrame[self.menu1.get()].dtypes==object):
                messagebox.showinfo(
                title='Error!',
                message= "Invalid data please select valid data"
                )  
                return
            plt.boxplot(self.dataFrame[self.menu1.get()])
            plt.get_current_fig_manager().canvas.set_window_title('Box Plot')
            plt.title(self.menu1.get().capitalize())
            plt.show()
        pass


class PieGraphBtn:
    def __init__(self, frame, font,dataFrame,menu1):
        self.dataFrame = dataFrame
        self.menu1 = menu1
        button = tk.Button(frame, text='Pie Chart', command=self.plot, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10,pady = 300)

    def plot(self):
        plt.close("all")
        if(self.menu1.get()=='Select the Column'):
            tk.messagebox.showinfo(
            title='Warning',
            message="No Column selected"
            )
        else:
            if(len(self.dataFrame)>500):
                y = Counter(self.dataFrame[self.menu1.get()][1:500])
            else:
                y = Counter(self.dataFrame[self.menu1.get()])

            sizes = list(y.values())
            labels = list(y.keys())
            
            fig1, ax1 = plt.subplots(figsize=(6, 5))
            fig1.subplots_adjust(0.3,0,1,1)

            theme = plt.get_cmap('twilight')
            ax1.set_prop_cycle("color", [theme(1. * i / len(sizes)) for i in range(len(sizes))])

            _, _ = ax1.pie(sizes, startangle=90)

            ax1.axis('equal')

            total = sum(sizes)
            plt.legend(
                loc='upper left',
                labels=['%s, %1.1f%%' % (
                    l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
                prop={'size': 11},
                bbox_to_anchor=(0.0, 1),
                bbox_transform=fig1.transFigure
            )
            plt.get_current_fig_manager().set_window_title('Pie Chart')
            plt.show()
        pass
    
class violinPlotnBtn:
    def __init__(self, frame, font,dataFrame,menu1):
        self.dataFrame = dataFrame
        self.menu1=menu1
        button = tk.Button(frame, text='Violin Plot', command=self.plot, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10,pady = 300)

    def plot(self):
        if(self.menu1.get()=='Select the Column'):
            tk.messagebox.showinfo(
            title='Warning',
            message="No Column selected"
            )
        else:
            # print(self.dataFrame[self.menu1.get()].dtypes)
            if(self.dataFrame[self.menu1.get()].dtypes==object):
                messagebox.showinfo(
                title='Error!',
                message= "Invalid data please select valid data"
                )  
                return
            plt.close("all")
            plt.violinplot(self.dataFrame[self.menu1.get()])
            plt.get_current_fig_manager().canvas.set_window_title('Violin Plot')
            plt.title(self.menu1.get().capitalize())
            plt.show()
        pass


def run(dataFrame):
    root = tk.Tk()
    root.title("Plot")
    root.config(bg="#84e9d9")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.state('zoomed')
    font = ("Helvetica",)
    root.option_add('*TCombobox*Listbox.font', font+(15,)) # apply font to combobox
    title(root,font)

    # get the columns name from the file
    lists = dataFrame.columns
    lists=lists.tolist()
    
    # Frame for option menu
    frameOptions = tk.Frame(root, bg="#84e9d9")
    frameOptions.pack(pady=0)

    frameBtns = tk.Frame(root, bg="#84e9d9")
    frameBtns.pack(pady=0)
    
    opts=StringVar(frameOptions)
    opts.set("Select the Column")

    men=ttk.Combobox(frameOptions, width=30, justify='center', height=len(lists),textvariable=opts,values=lists ,font=font+(16,))
    men.option_add('*TCombobox*Listbox.Justify', 'center')
    men.place(x=350,y=80,width=250)
    men.pack()
    name = men.get()
    pltBtnHisto = HistogramBtn(frameBtns, font, dataFrame,men)
    pltBtnBar = BarGraphBtn(frameBtns, font, dataFrame,men)
    pltBtnBoxPlot = BoxPlotGraphBtn(frameBtns, font, dataFrame,men)
    pltBtnpie = PieGraphBtn(frameBtns, font, dataFrame,men)
    pltBtnViolin = violinPlotnBtn(frameBtns, font, dataFrame,men)
    

    root.mainloop()
