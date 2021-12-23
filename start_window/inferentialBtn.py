try :
    from inferential_window.inferential_window import run
except:
    import sys
    sys.path.append('inferential_window')
    from inferential_window import run

import tkinter as tk



class inferentialBtn:
    def __init__(self, frame, font,dataFrame):
        self.dataFrame = dataFrame
        button = tk.Button(frame, text='Inferential', command=self.plotData, font=font + (20,), bg="#4b50b0",
                           fg="#efefef",width = 10)
        button.pack(side=tk.LEFT,padx = 10)

    def plotData(self):
        run(self.dataFrame)
