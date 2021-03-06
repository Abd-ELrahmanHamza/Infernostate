try :
    from probability_window.probability_window import run
except:
    import sys
    sys.path.append('probability_window')
    from probability_window import run

import tkinter as tk



class probabilityBtn:
    def __init__(self, frame, font,dataFrame):
        self.dataFrame = dataFrame
        button = tk.Button(frame, text='Probability', command=self.plotData, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10)

    def plotData(self):
        run(self.dataFrame)
