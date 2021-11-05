import tkinter as tk
from probability_window.probability_window import run


class probabilityBtn:
    def __init__(self, frame, font,dataFrame):
        self.dataFrame = dataFrame
        button = tk.Button(frame, text='probability', command=self.plotData, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10)

    def plotData(self):
        run(self.dataFrame)
