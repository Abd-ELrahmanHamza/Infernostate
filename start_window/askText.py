import tkinter as tk

class askText:
    def __init__(self,root,font):
        topFrame = tk.Frame(root)
        topFrame.pack(pady=20)
        label = tk.Label(topFrame,text = "Choose a file to start the journey",font=font+(30,),fg="#4b50b0",bg="#84e9d9")
        label.pack()
