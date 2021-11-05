import tkinter as tk
def run(dataFrame):
    root = tk.Tk()
    root.title("Infernostate")
    root.config(bg="#84e9d9")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.state('zoomed')

    # your code here
    lbl = tk.Label(root,text = "plot")
    lbl.pack()
    print(dataFrame)

    root.mainloop()
