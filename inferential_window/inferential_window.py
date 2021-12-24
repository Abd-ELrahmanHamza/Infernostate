import tkinter as tk
from scipy import stats
import numpy as np
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot as plt
from collections import Counter


# Title of the window
class title:
    def __init__(self, root, font):
        topFrame = tk.Frame(root)
        topFrame.pack(side=tk.TOP, pady=40)
        label = tk.Label(topFrame, text="Inferential", font=font + (40, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack()



class CLTBtn:
    def __init__(self, frame, font,txtNumberOfSamples,txtSizeOfSamp,dataFrame,comboMen):
        self.txtNumberOfSamples = txtNumberOfSamples
        self.txtSizeOfSamp = txtSizeOfSamp
        self.dataFrame = dataFrame
        self.combMen = comboMen
        button = tk.Button(frame, text='CLT', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        numSamples = self.txtNumberOfSamples.getParameter().get('1.0', 'end')
        sampSize = self.txtSizeOfSamp.getParameter().get('1.0', 'end')
        # print(numSamples,sampSize)
        try:
            numSamples = int(numSamples)
            sampSize = int(sampSize)
        except:
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data.. All values set to zero"
            )

        if (self.combMen.get() == "Select the Column"):
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data"
            )
        else:
            # print(sampSize,numSamples)
            means = [np.mean(self.dataFrame.sample(n=sampSize)[self.combMen.get()]) for _i in range(numSamples)]
            # print(means)
            plt.hist(means, color='maroon')
            plt.get_current_fig_manager().canvas.set_window_title('Histogram')
            plt.title(self.combMen.get().capitalize())
            plt.xlabel('Values')
            plt.ylabel('Frequency')
            plt.show()


class CLTSizeSample:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="Size of each sample ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class CLTNumSamples:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="Number of samples ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
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

    titleWindow = title(root,font)

    ##################################################################################
    #   comboBox Start
    ##################################################################################
    lists = dataFrame.columns
    lists = lists.tolist()

    # Frame for option menu
    frameOptions = tk.Frame(root, bg="#84e9d9")
    frameOptions.pack(pady=0)

    frameBtns = tk.Frame(root, bg="#84e9d9")
    frameBtns.pack(pady=0)

    opts = tk.StringVar(frameOptions)
    opts.set("Select the Column")

    men = ttk.Combobox(frameOptions, width=30, justify='center', height=len(lists), textvariable=opts, values=lists,
                       font=font + (16,),state = "readonly")
    men.option_add('*TCombobox*Listbox.Justify', 'center')
    men.place(x=350, y=80, width=250)
    men.pack()
    ##################################################################################
    #   comboBox END
    ##################################################################################

    frameCLT = tk.Frame(root, bg="#84e9d9")
    frameCLT.pack(padx=20, pady=30)
    CLTSize = CLTSizeSample(frameCLT, font)
    CLTNum = CLTNumSamples(frameCLT, font)
    CLTBtn(frameCLT, font, CLTNum, CLTSize, dataFrame, men)


    root.mainloop()
