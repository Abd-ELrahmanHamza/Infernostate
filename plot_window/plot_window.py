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
        plt.hist(self.dataFrame[self.menu1.get()],color = 'maroon')
        # var1=plt.figure(1)
        # var1.canvas.set_window_title('Histogram')
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
        plt.hist(self.dataFrame[self.menu1.get()],color = 'maroon',rwidth=0.5)
        # var2=plt.figure(1)
        # var2.canvas.set_window_title('Bar Chart')
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
        plt.boxplot(self.dataFrame[self.menu1.get()])
        # var3=plt.figure(1)
        # var3.canvas.set_window_title('Box Plot')
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
        # colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7))
        # self.dataFrame=self.dataFrame[self.menu1.get()].tolist()
        # plt.pie(self.dataFrame[self.menu1.get()][1:500], frame=True)
        # plt.get_current_fig_manager().canvas.set_window_title('Pie Chart')
        # plt.title(self.menu1.get().capitalize())
        
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
    # print(lists)
    lists=lists.tolist()
    
    # Frame for option menu
    frameOptions = tk.Frame(root, bg="#84e9d9")
    frameOptions.pack(pady=0)

    frameBtns = tk.Frame(root, bg="#84e9d9")
    frameBtns.pack(pady=0)
    
    opts=StringVar(frameOptions)
    opts.set("Select the Column")
    # root, width=27, height=3, textvariable=n, values=options
    # text_font = ('Courier New', '10')
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
    
    # def showComb():
    #     n = tk.StringVar()
    #     global chartchoosen
    #     chartchoosen = ttk.Combobox(
    #         root, width=27, height=3, textvariable=n, values=options)
    #     ttk.Label(root, text="Select Chart:", font=(
    #         "Helvetica", 10)).place(rely=0.5, relx=0.4, anchor=CENTER)
    #     chartchoosen.place(rely=0.5, relx=0.5, anchor=CENTER)
    #     # chartchoosen.pack()
    #     chartchoosen.current()
    #     if chartchoosen.get() != "":
    #         messagebox.showinfo(chartchoosen.get())

    # def menu():
    #     showComb()
    #     btn2 = tk.Button(root, text="Get Chart", bg="#4b50b0", fg="#efefef", font=("Helvetica", 10),
    #                      width=7, command=checkcomb).place(relx=0.6, rely=0.5, anchor=CENTER)

    # def checkcomb():
    #     if chartchoosen.get() == 'Bar Char':
    #         plt.bar(dataFrame.values.tolist())
    #         plt.show()
    #     elif chartchoosen.get() == "Dot Digram":
    #         plt.plot(dataFrame.values.tolist(), 'ro')
    #         plt.xlabel('Frequency')
    #         plt.ylabel('Values')
    #         plt.show()
    #     elif chartchoosen.get() == "Box plot":
    #         plt.boxplot(dataFrame.values.tolist())
    #         plt.show()
    #     elif chartchoosen.get() == "Histogram":
    #         plt.hist(dataFrame.values.tolist())
    #         plt.show()
    #     else:
    #         # sg.stem_graphic(x, scale=10)
    #         plt.pie(dataFrame.values.tolist())
    #         plt.show()

    # # root.tk.title("Charts")
    # # root.configure(bg='#84e9d9')
    # # root.geometry("600x400")
    # btn = tk.Button(root, text="Charts Menu", bg="#4b50b0", fg="#efefef", width=10, height=1,
    #                 command=menu).place(relx=0.5, rely=0.4, anchor=CENTER)
    # lbl = tk.Label(root, text="plot")
    # lbl.pack()
    # print(dataFrame.values.tolist())
    root.mainloop()
