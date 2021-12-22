import tkinter as tk
from tkinter import *
from tkinter import ttk
from scipy import stats
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


pmfValueN = 0
pmfValueP = 0
pmfValueX = 0
class title:
    def __init__(self, root, font):
        topFrame = tk.Frame(root)
        topFrame.pack(side=tk.TOP, pady=40)
        label = tk.Label(topFrame, text="Probability", font=font + (40, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack()


class pmfBtn:
    def __init__(self, frame, font,txtPmfN,txtPmfP,txtPmfX,labelPmf):
        self.txtPmfN = txtPmfN
        self.txtPmfP = txtPmfP
        self.txtPmfX = txtPmfX
        self.labelPmf = labelPmf
        button = tk.Button(frame, text='pmf', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global pmfValueN
        global pmfValueP
        global labelPmf
        pmfValueN = self.txtPmfN.getParameter().get('1.0', 'end')
        pmfValueP = self.txtPmfP.getParameter().get('1.0', 'end')
        pmfValueX = self.txtPmfX.getParameter().get('1.0', 'end')
        try:
            pmfValueN = float(pmfValueN)
            pmfValueP = float(pmfValueP)
            pmfValueX = float(pmfValueX)
        except:
            pmfValueN = 0
            pmfValueP = 0
            pmfValueX = 0
            print("Hello")
        # pmfValueP = int(pmfValueP)
        # pmfValueP = int(pmfValueP)
        print(pmfValueN,pmfValueP,pmfValueX)
        X = stats.binom(pmfValueN, pmfValueP)  # Declare X to be a binomial random variable
        self.labelPmf.config(text = "PMF = "+str(X.pmf(pmfValueX)))
        print(X.pmf(pmfValueX))



class pmfTextBoxN:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="N", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class pmfTextBoxP:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="P", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T
class pmfTextBoxX:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T



def run(dataFrame):
    root = tk.Tk()
    root.title("Probability")
    root.config(bg="#84e9d9")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.state('zoomed')
    font = ("Helvetica",)
    root.option_add('*TCombobox*Listbox.font', font + (15,))

    # title of window
    title(root, font)



    framePmf = tk.Frame(root, bg="#84e9d9")
    framePmf.pack(padx = 20)
    txtPmfN = pmfTextBoxN(framePmf, font)
    txtPmfP = pmfTextBoxP(framePmf, font)
    txtPmfX = pmfTextBoxX(framePmf, font)
    labelPmf = tk.Label(framePmf, text="PMF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    pmfBtn(framePmf, font,txtPmfN,txtPmfP,txtPmfX,labelPmf)
    labelPmf.pack(side=tk.LEFT, padx=10)

    # your code here

    root.mainloop()
