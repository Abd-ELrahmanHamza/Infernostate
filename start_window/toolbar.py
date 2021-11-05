import tkinter as tk


class file_subMenu:
    def __init__(self, menu):
        fileSubMenu = tk.Menu(menu)
        menu.add_cascade(label="file", menu=fileSubMenu)

        # create item in file
        fileSubMenu.add_command(label="new", command=self.file_NewCommand)
        fileSubMenu.add_separator()

    def file_NewCommand(self):
        print("file -> new")


class help_subMenu:
    def __init__(self, menu):
        helpSubMenu = tk.Menu(menu)
        menu.add_cascade(label="help", menu=helpSubMenu)

        # create item in file
        helpSubMenu.add_command(label="? help", command=self.help_helpCommand)
        helpSubMenu.add_separator()

    def help_helpCommand(self):
        print("help -> help")


class toolbar:
    def __init__(self, root):
        menu = tk.Menu(root)
        root.config(menu=menu)
        file_subMenu(menu)
        help_subMenu(menu)
