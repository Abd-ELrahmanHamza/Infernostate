import tkinter as tk
from tkinter import filedialog as fd
import pandas


class fileButton:
    def __init__(self, root, font):
        self.__filetypes = (
            ('CSV files', '*.csv'),
        )
        self.__filename = ""
        self.dataFrame = ""
        frame = tk.Frame(root)
        frame.pack(pady=30)
        button = tk.Button(root, text='Open a File', command=self.fileSelect, font=font + (20,), bg="#4b50b0",
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
            print(self.dataFrame)
