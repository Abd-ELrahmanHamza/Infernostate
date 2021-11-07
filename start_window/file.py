import tkinter as tk
from tkinter import filedialog as fd
import pandas
from plotBtn import plotBtn
from centerBtn import centerBtn
from inferentialBtn import inferentialBtn
from probabilityBtn import probabilityBtn

class fileButton:
    def __init__(self, root, font):
        self.__filetypes = (
            ('CSV files', '*.csv'),
        )
        self.__root = root
        self.__font = font
        self.__filename = ""
        self.dataFrame = ""
        frame = tk.Frame(root)
        frame.pack(pady=30)
        button = tk.Button(frame, text='Open a File', command=self.fileSelect, font=font + (20,), bg="#4b50b0",
                           fg="#efefef")
        button.pack()

    def fileSelect(self):
        self.__filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=self.__filetypes)

        tk.messagebox.showinfo(
            title='Selected File',
            message=self.__filename if self.__filename != "" else "No file selected"
        )
        self.read_file()

    def read_file(self):
        if self.__filename != "":
            self.dataFrame = pandas.read_csv(self.__filename)
            frameBtns = tk.Frame(self.__root,bg="#84e9d9")
            frameBtns.pack(pady=30)
            pltBtn = plotBtn(frameBtns,self.__font,self.dataFrame)
            cntrBtn = centerBtn(frameBtns,self.__font,self.dataFrame)
            infrBtn = inferentialBtn(frameBtns,self.__font,self.dataFrame)
            probBtn = probabilityBtn(frameBtns,self.__font,self.dataFrame)