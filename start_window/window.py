import tkinter as tk
from toolbar import toolbar
from title import title
from file import fileButton
from askText import askText

root = tk.Tk()
root.title("Infernostate")
root.config(bg="#84e9d9")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.state('zoomed')

font = ("Helvetica",)
tool_bar = toolbar(root)
title = title(root, font)
askText = askText(root, font)
fileButton = fileButton(root, font)

root.mainloop()
