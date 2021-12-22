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

cdfValueN = 0
cdfValueP = 0
cdfValueX = 0

lambdaPoss = 0
possionX = 0
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
        button = tk.Button(frame, text='PMF', command=self.calculate, font=font + (20,), bg="#4b50b0",
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



class cdfBtn:
    def __init__(self, frame, font,txtCdfN,txtCdfP,txtCdfX,labelCdf):
        self.txtCdfN = txtCdfN
        self.txtCdfP = txtCdfP
        self.txtCdfX = txtCdfX
        self.labelCdf = labelCdf
        button = tk.Button(frame, text='CDF', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global cdfValueX
        global cdfValueP
        global cdfValueN
        cdfValueN = self.txtCdfN.getParameter().get('1.0', 'end')
        cdfValueP = self.txtCdfP.getParameter().get('1.0', 'end')
        cdfValueX = self.txtCdfX.getParameter().get('1.0', 'end')
        try:
            cdfValueX = float(cdfValueX)
            cdfValueP = float(cdfValueP)
            cdfValueN = float(cdfValueN)
        except:
            cdfValueN = 0
            cdfValueP = 0
            cdfValueX = 0
            print("Hello")
        # pmfValueP = int(pmfValueP)
        # pmfValueP = int(pmfValueP)
        print(cdfValueN,cdfValueP,cdfValueX)
        X = stats.binom(cdfValueN, cdfValueP)  # Declare X to be a binomial random variable
        self.labelCdf.config(text = "CDF = "+str(X.cdf(cdfValueX)))
        # print(X.cdf(pmfValueX))



class cdfTextBoxN:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="N", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class cdfTextBoxP:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="P", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T
class cdfTextBoxX:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T



class possionBtn:
    def __init__(self, frame, font,txtlambda,txtPossionX,labelpossion):
        self.txtlambda = txtlambda
        self.txtPossionX = txtPossionX
        self.labelCdf = labelpossion
        button = tk.Button(frame, text='poisson PMF', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global lambdaPoss
        lambdaPoss = self.txtlambda.getParameter().get('1.0', 'end')
        possionX = self.txtPossionX.getParameter().get('1.0', 'end')
        try:
            lambdaPoss = float(lambdaPoss)
            possionX = float(possionX)
        except:
            lambdaPoss = 0
            possionX = 0
            print("Hello")
        print(lambdaPoss,possionX)
        X = stats.poisson(lambdaPoss)  # Declare X to be a binomial random variable
        self.labelCdf.config(text = "PMF = "+str(X.pmf(possionX)))



class lambdaPossion:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="lambda ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class xPossion:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
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
    framePmf.pack(padx = 20,pady=30)
    txtPmfN = pmfTextBoxN(framePmf, font)
    txtPmfP = pmfTextBoxP(framePmf, font)
    txtPmfX = pmfTextBoxX(framePmf, font)
    labelPmf = tk.Label(framePmf, text="Binomial PMF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    pmfBtn(framePmf, font,txtPmfN,txtPmfP,txtPmfX,labelPmf)
    labelPmf.pack(side=tk.LEFT, padx=10)


    frameCdf = tk.Frame(root, bg="#84e9d9")
    frameCdf.pack(padx = 20,pady=30)
    txtCdfN = cdfTextBoxN(frameCdf, font)
    txtCdfP = cdfTextBoxP(frameCdf, font)
    txtCdfX = cdfTextBoxX(frameCdf, font)
    labelCdf = tk.Label(frameCdf, text="Binomial CDF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    cdfBtn(frameCdf, font,txtCdfN,txtCdfP,txtCdfX,labelCdf)
    labelCdf.pack(side=tk.LEFT, padx=10)



    framePossion = tk.Frame(root, bg="#84e9d9")
    framePossion.pack(padx = 20,pady=30)
    txtlambda = lambdaPossion(framePossion, font)
    txtPossionX = xPossion(framePossion, font)
    labelPossion = tk.Label(framePossion, text="Possion PMF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    possionBtn(framePossion, font,txtlambda,txtPossionX,labelPossion)
    labelPossion.pack(side=tk.LEFT, padx=10)
    # your code here

    root.mainloop()
