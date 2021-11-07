import tkinter as tk
from tkinter import Listbox, ttk
from tkinter.constants import CENTER
from typing import Text
import matplotlib.pyplot as plt
import plotly.express as pe
import numpy as np
import pandas as pd
# import steamgraphic as sg
from tkinter import messagebox
from numpy.lib.function_base import place
options = ['Bar Char', 'Histogram', 'Dot Digram',
           'Box plot', 'Stem-and-leaf Plot']


def run(dataFrame):
    root = tk.Tk()
    root.title("Infernostate")
    root.config(bg="#84e9d9")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.state('zoomed')

    def showComb():
        n = tk.StringVar()
        global chartchoosen
        chartchoosen = ttk.Combobox(
            root, width=27, height=3, textvariable=n, values=options)
        ttk.Label(root, text="Select Chart:", font=(
            "Helvetica", 10)).place(rely=0.5, relx=0.4, anchor=CENTER)
        chartchoosen.place(rely=0.5, relx=0.5, anchor=CENTER)
        # chartchoosen.pack()
        chartchoosen.current()
        if chartchoosen.get() != "":
            messagebox.showinfo(chartchoosen.get())

    def menu():
        showComb()
        btn2 = tk.Button(root, text="Get Chart", bg="#4b50b0", fg="#efefef", font=("Helvetica", 10),
                         width=7, command=checkcomb).place(relx=0.6, rely=0.5, anchor=CENTER)

    def checkcomb():
        if chartchoosen.get() == 'Bar Char':
            plt.bar(dataFrame.values.tolist())
            plt.show()
        elif chartchoosen.get() == "Dot Digram":
            plt.plot(dataFrame.values.tolist(), 'ro')
            plt.xlabel('Frequency')
            plt.ylabel('Values')
            plt.show()
        elif chartchoosen.get() == "Box plot":
            plt.boxplot(dataFrame.values.tolist())
            plt.show()
        elif chartchoosen.get() == "Histogram":
            plt.hist(dataFrame.values.tolist())
            plt.show()
        else:
            # sg.stem_graphic(x, scale=10)
            plt.pie(dataFrame.values.tolist())
            plt.show()

    # root.tk.title("Charts")
    # root.configure(bg='#84e9d9')
    # root.geometry("600x400")
    btn = tk.Button(root, text="Charts Menu", bg="#4b50b0", fg="#efefef", width=10, height=1,
                    command=menu).place(relx=0.5, rely=0.4, anchor=CENTER)
    lbl = tk.Label(root, text="plot")
    lbl.pack()
    print(dataFrame.values.tolist())
    root.mainloop()
