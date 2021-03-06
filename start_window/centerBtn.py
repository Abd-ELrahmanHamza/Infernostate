try :
    from center_window.center_window import run
except:
    import sys
    sys.path.append('center_window')
    from center_window import run

import tkinter as tk



class centerBtn:
    def __init__(self, frame, font,dataFrame):
        self.dataFrame = dataFrame
        button = tk.Button(frame, text='Measure of center', command=self.plotData, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 15)
        button.pack(side=tk.LEFT,padx = 10)

    def plotData(self):
        run(self.dataFrame)
