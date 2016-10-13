import tkinter as tk


class Application():
    def __init__(self):
        self.root = tk.Tk()
        Bquit = tk.Button(self.root, text = "quit")
        Bcreate = tk.Button(self.root, text = "create grid")
        Brandom = tk.Button(self.root, text = "create random")
        Bhelp = tk.Button(self.root, text = "help")
        Lwelcome = tk.Label(self.root, text = """welcome to the transportation
problem solver!""")
        Lrows = tk.Label(self.root,text = "rows")
        Lcolumns = tk.Label(self.root,text = "columns")
        Erows = tk.Entry(self.root)
        Ecolumns  = tk.Entry(self.root)

        Lwelcome.pack()
        Lrows.pack()
        Erows.pack()
        Lcolumns.pack()
        Ecolumns.pack()
        Bcreate.pack()
        Brandom.pack()
        Bquit.pack()
        Bhelp.pack()

        self.root.mainloop()
        

app = Application()
