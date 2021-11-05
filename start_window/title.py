import tkinter as tk


class title:
    def __init__(self, root, font):
        topFrame = tk.Frame(root)
        topFrame.pack(side=tk.TOP, pady=40)
        label = tk.Label(topFrame, text="Infernostate", font=font + (40, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack()
