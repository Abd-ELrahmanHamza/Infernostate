import tkinter as tk
from tkinter import filedialog as fd
import pandas
class fileButton:
    def __init__(self,root,font):
        self.filetypes =()
        self.filename=""
        self.dataFrame = ""
        frame = tk.Frame(root)
        frame.pack(pady = 30)
        button = tk.Button(root,text='Open a File',command=self.fileSelect,font=font+(20,),bg="#4b50b0",fg="#efefef")
        button.pack()

    def fileSelect(self):
        filetypes = (
            ('CSV files', '*.csv'),
        )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        tk.messagebox.showinfo(
            title='Selected File',
            message=self.filename
        )
        self.read_file()
    def read_file(self):
        import pandas
        self.dataFrame = pandas.read_csv(self.filename)
        print(self.dataFrame)